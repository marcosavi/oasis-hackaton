from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_certificate, name='generate_certificate'),
    path('display/<int:id>/', views.certificate_display, name='certificate_display'),
]