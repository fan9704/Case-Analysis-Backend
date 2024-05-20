from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Patient
from api.serializers.patient import PatientGeneralSerializer


class PatientListCreateAPIView(ListCreateAPIView):
    serializer_class = PatientGeneralSerializer
    queryset = Patient.objects.all()


class PatientReadUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientGeneralSerializer
    queryset = Patient.objects.all()
