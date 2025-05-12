from django.urls import path
from . import views


urlpatterns = [
    path("<uuid:uuid>/", views.SendInquiryView.as_view(), name="send_inquiry"),
    path("", views.SendInquiryView.as_view(), name="send_inquiry"),
]
