from django.urls import path, include

urlpatterns = [
    path("gpt/", include("api.controllers.gpt")),
    path("pathology/", include("api.controllers.pathology")),
    path("case/", include("api.controllers.case")),
    path("judge/", include("api.controllers.judge")),
]
