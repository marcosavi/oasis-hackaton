from django.urls import path
from . import views

app_name = "edu"

urlpatterns = [
    path("", views.index, name = "index"),
    path("teacher/1/", views.classSize, name = "class-size"),
    path("teacher/2/", views.studentsAge, name = "students-age"),
    path("teacher/3/", views.tools, name = "tools"),
    path("teacher/4/", views.fetching, name = "fetching"),
    path("teacher/ptsd-course/", views.ptsdCourse, name = "ptsd"),
    path("teacher/dashboard/", views.dashboard, name = "dashboard"),
    path("future-teachers/", views.futureTeachers, name = "future-teachers"),
]