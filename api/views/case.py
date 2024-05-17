from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Case
from api.serializers.case import CaseGeneralSerializer


class CaseListCreateAPIView(ListCreateAPIView):
    serializer_class = CaseGeneralSerializer
    queryset = Case.objects.all()


class CaseReadUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CaseGeneralSerializer
    queryset = Case.objects.all()
