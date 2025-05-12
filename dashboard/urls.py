from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path(
        "medication-requests/<str:number>/",
        views.EvaluateMedicationRequestView.as_view(),
        name="evaluate-medication-request",
    ),
    path(
        "medication-requests/",
        views.EvaluateMedicationRequestView.as_view(),
        name="evaluate-medication-request",
    ),
]
