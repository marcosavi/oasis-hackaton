from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    courses = Course.objects.all()
    return render(request, "courses/index.html", {'courses': courses})

@login_required
def course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course.html', {'course': course})

@login_required
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:index')
    else:
        form = CourseForm()
    return render(request, 'courses/add.html', {'form': form})
