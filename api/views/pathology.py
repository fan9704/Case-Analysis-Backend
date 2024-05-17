import json

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers.pathology import PathologyGeneralSerializer
from api.models import Patient
from api.serializers.case import CaseGeneralSerializer
from api.utils.gpt_client import GPTClient
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Pathology

gpt = GPTClient()


class PathologyListCreateAPIView(ListCreateAPIView):
    serializer_class = PathologyGeneralSerializer
    queryset = Pathology.objects.all()


class PathologyToCaseAPIView(APIView):
    def get(self, request, pk):
        pathology = Pathology.objects.get(pk=pk)
        response = gpt.pathologyToCase(pathology)
        res = json.loads(response.content)

        res["user"] = res["user_id"]
        del res["user_id"]

        case = CaseGeneralSerializer(data=res)
        case.is_valid(raise_exception=True)
        case.save()
        return Response(res, status=200)
