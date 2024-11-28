from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.index, name = "index"),
    path('<slug:slug>/', views.course, name = "course"),
    path('display/<int:id>/', views.certificate_display, name='conclusion'),
]