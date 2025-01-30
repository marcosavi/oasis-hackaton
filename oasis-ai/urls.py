from django.urls import path
from . import views

app_name = "oasis-chat"

urlpatterns = [
    path("", views.index, name = "index"),
    path("chat/", views.ollama_chat, name = "ollama_chat"),
    path("translate/", views.ollama_translate, name="ollama_translate"),
]