from django.urls import path
from inquiry import views

app_name = "api"
urlpatterns = [
    path("products/", views.ProductsListView.as_view(), name="products"),
    path("doctors/", views.DoctorsListView.as_view(), name="doctors"),
    path("users/", views.UserView.as_view(), name="users"),
    path("submit-form/", views.SubmitFormView.as_view(), name="submit-form"),
]
