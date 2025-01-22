from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.index, name="index"),
    path("educators/", views.course, name="course"),
    path("display/<str:filename>/", views.certificate_display, name="conclusion"),  # Certificate display
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
