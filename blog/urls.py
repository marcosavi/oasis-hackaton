from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name = "index"),
    path("translanguaging/", views.translanguaging, name = "translanguaging"),
    path("arabizi/", views.arabizi, name = "arabizi"),
    path("codeswitching/", views.codeswitching, name = "codeswitching"),
    path("whitedialects/", views.whitedialects, name = "whitedialects"),
]