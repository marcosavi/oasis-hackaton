from django.urls import path
from . import views

app_name = "edu"

urlpatterns = [
    path("", views.index, name="index"),
    path("teachers/", views.teachers, name="teachers"),
    path("teachers/class-size/", views.classSize, name="class-size"),
    path("teachers/students-age/", views.studentsAge, name="students-age"),
    path("teachers/tools/", views.tools, name="tools"),
    path("teachers/fetching/", views.fetching, name="fetching"),
    path("teachers/dashboard/", views.dashboard, name="dashboard"),
    path("future-teachers/", views.futureTeachers, name="future-teachers"),
    path("courses/<int:course_id>/", views.courseDetail, name="course_detail"),
    path("courses/<int:course_id>/<int:chapter_id>/", views.chapterDetail, name="chapter_detail"),
]
