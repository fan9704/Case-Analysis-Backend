from django.urls import path, include
from api.views.case import CaseListCreateAPIView, CaseReadUpdateDeleteAPIView

urlpatterns = [
    # CaseRoutes
    path("", CaseListCreateAPIView.as_view(), name="case-list-create"),
    path(
        "<int:pk>/",
        CaseReadUpdateDeleteAPIView.as_view(),
        name="case-read-update-delete",
    ),
]
