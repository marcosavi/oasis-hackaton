from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('edu/', include('edu.urls')),
    path('login/', views.login.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('ai/', include('oasis-ai.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)