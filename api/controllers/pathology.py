from django.urls import path, include
from api.views.pathology import PathologyListCreateAPIView, PathologyToCaseAPIView

urlpatterns = [
    # Pathology Routes
    path("", PathologyListCreateAPIView.as_view(), name="pathology-list-create"),
    path(
        "convert/<int:pk>/", PathologyToCaseAPIView.as_view(), name="pathology-to-case"
    ),
]
