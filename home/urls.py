from django.urls import path # type: ignore
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name = "index"),
    path("donate/", views.donate, name = "donate"),
]