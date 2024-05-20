from django.urls import path, include
from api.views.pathology import (
    PathologyListCreateAPIView,
    PathologyToCaseAPIView,
    PathologyRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Pathology Routes
    path("", PathologyListCreateAPIView.as_view(), name="pathology-list-create"),
    path(
        "<int:pk>/",
        PathologyRetrieveUpdateDestroyAPIView.as_view(),
        name="pathology-RUD",
    ),
    path(
        "convert/<int:pk>/", PathologyToCaseAPIView.as_view(), name="pathology-to-case"
    ),
]
