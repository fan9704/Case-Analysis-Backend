from django.urls import path, include
from api.views.patient import  PatientListCreateAPIView,PatientReadUpdateDeleteAPIView
urlpatterns = [
    # Patient Routes
    path("", PatientListCreateAPIView.as_view(), name="patient-list-create"),
    path(
        "<int:pk>/",
        PatientReadUpdateDeleteAPIView.as_view(),
        name="patient-read-update-delete",
    ),
]
