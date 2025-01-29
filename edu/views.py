from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Course, Chapter, Quiz, Question, Alternative

# Create your views here.
def index(request):
    return render(request, "edu/index.html", {})

def teachers(request):
    return render(request, "edu/teachers/teachers.html", {})

def classSize(request):
    return render(request, "edu/teachers/class-size.html", {})

def studentsAge(request):
    return render(request, "edu/teachers/students-age.html", {})

def tools(request):
    return render(request, "edu/teachers/tools.html", {})

def fetching(request):
    return render(request, "edu/teachers/fetching.html", {})

def dashboard(request):
    return render(request, "edu/teachers/dashboard.html", {})

def futureTeachers(request):
    return render(request, "edu/future-teachers/future-teachers.html", {})

def courseDetail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    chapters = course.chapters.all()
    chapters_with_quiz = [chapter for chapter in chapters if hasattr(chapter, 'quiz')]
    return render(request, "edu/courses/course.html", {
        "course": course,
        "chapters": chapters,
        "chapters_with_quiz": chapters_with_quiz,
    })

def chapterDetail(request, course_id, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id, course_id=course_id)
    return render(request, "edu/courses/chapter.html", {"chapter": chapter})