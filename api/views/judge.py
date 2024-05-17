from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.model.case import Case
from api.utils.gpt_client import GPTClient

gpt = GPTClient()


class JudgeTwoCaseAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "case1_id",
                openapi.IN_PATH,
                description="The ID of case1",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "case2_id",
                openapi.IN_PATH,
                description="The ID of case2",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def get(self, request, case1_id: int, case2_id: int):
        case1 = Case.objects.get(id=case1_id)
        case2 = Case.objects.get(id=case2_id)
        response = gpt.judgeTwoCase(case1, case2)
        return Response(response, status=200)
