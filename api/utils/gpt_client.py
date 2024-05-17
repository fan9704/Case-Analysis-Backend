import os
import openai
from api.models import Pathology, Case
from api.serializers.pathology import PathologyGeneralSerializer
from api.serializers.case import CaseGeneralSerializer


class GPTClient:
    api_key = "請輸入 API Key"

    def __init__(self):
        if not self.api_key:
            raise Exception("GPT_API_KEY is not set")
        print(self.api_key)
        openai.api_key = self.api_key
        self.client = openai.OpenAI()

    def send(self, msg: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
                },
                {
                    "role": "user",
                    "content": "Compose a poem that explains the concept of recursion in programming.",
                },
            ],
        )

        return response.choices[0].message

    def pathologyToCase(self, pathology: Pathology):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """你是一個協助將 Pathology 轉換成 Case 的助手，你可以幫助使用者將 Pathology 轉換成 Case 空白的欄位內容請隨機生成。且只以 JSON 回答 格式如下 {
    "user_id": 1,
    "background": "乳腺組織切片，大小5cm x 3cm。",
    "clinical_findings": "顯示乳腺細胞異常增生，可能為乳癌。",
    "diagnostic_process": "進行了超聲波和MRI檢查，結果支持初步診斷。",
  "intervention_and_treatment": "建議進行手術治療，具體方案待醫師決定。",
  "outcome": "目前無法確定病變的完全狀態，需進一步觀察。",
  "discuss": "建議與專科醫師進行多學科討論，以確保最佳治療計劃。",
    "pathology": "初步診斷為乳腺癌，需要進一步檢查。"
}不知道的欄位內容請造假不要留空。""",
                },
                {
                    "role": "user",
                    "content": f"""{PathologyGeneralSerializer(pathology).data},
                """,
                },
            ],
        )

        return response.choices[0].message

    def judgeTwoCase(self, case1: Case, case2: Case):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """你是一個分析病例得系統，你將會收到兩個病例 JSON，請幫我分析差異給予重點""",
                },
                {
                    "role": "user",
                    "content": f"""case1: {CaseGeneralSerializer(case1).data}, case2 {CaseGeneralSerializer(case2).data}""",
                },
            ],
        )

        return response.choices[0].message
