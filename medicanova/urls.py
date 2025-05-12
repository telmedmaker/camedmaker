from django.urls import path, include
from django.contrib import admin
from two_factor.urls import urlpatterns as tf_urls
from two_factor.views import LoginView
from two_factor.admin import AdminSiteOTPRequired
from django.contrib.auth.views import LogoutView

admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/login/", LoginView.as_view(), name="login"),
    path("account/logout/", LogoutView.as_view(), name="logout"),
    path("fragebogen/", include("inquiry.urls")),
    path("api/v1/", include("api.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("blueten/", include("blooms.urls")),
]
