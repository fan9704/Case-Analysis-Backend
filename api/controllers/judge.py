from django.urls import path, include
from api.views.judge import JudgeTwoCaseAPIView

urlpatterns = [
    # Judge Routes
    path("<int:case1_id>/<int:case2_id>/", JudgeTwoCaseAPIView.as_view(), name="gpt"),
]
