from django.urls import path
from . import views


app_name = "blooms"
urlpatterns = [
    path("", views.BloomsOverview.as_view(), name="blooms"),
]
