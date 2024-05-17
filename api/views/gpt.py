from api.utils.gpt_client import GPTClient
from api.serializers.gpt import GPTRequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

client = GPTClient()


class GPTView(APIView):
    @swagger_auto_schema(
        request_body=GPTRequestSerializer,
    )
    def post(self, request):
        msg = request.data.get("msg")
        res = client.send(msg)
        return Response({"response": res})
