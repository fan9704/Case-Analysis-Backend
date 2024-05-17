from django.urls import path, include
from api.views.gpt import GPTView

urlpatterns = [
    # GPT Routes
    path("", GPTView.as_view(), name="gpt"),
]
