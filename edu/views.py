from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from .models import Course, Chapter, StudentProfile
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm  
from django.utils import timezone
from django.contrib import messages

# Create your views here.
class login(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            return reverse_lazy('edu:index')
        return reverse_lazy('edu:index')
    
@login_required
def courseDetail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    chapters = Chapter.objects.filter(course=course)
    chapters_with_quiz = [chapter for chapter in chapters if hasattr(chapter, 'quiz')]
    return render(request, "edu/courses/course.html", {
        "course": course,
        "chapters": chapters,
        "chapters_with_quiz": chapters_with_quiz,
    })

@login_required
def chapterDetail(request, course_id, order):
    chapter = get_object_or_404(Chapter, course_id=course_id, order=order)
    next_chapter = Chapter.objects.filter(
        course=chapter.course, order__gt=chapter.order
    ).order_by('order').first()
    questions = chapter.quiz.questions.all() if hasattr(chapter, 'quiz') else []
    return render(request, "edu/courses/chapter.html", {
        "chapter": chapter,
        "quiz": getattr(chapter, 'quiz', None),
        "questions": questions,
        "next_chapter": next_chapter,
        "course": chapter.course,
    })

def process_quiz(request):
    if request.method == "POST":
        selected_course_ids = request.POST.getlist("selected_courses")
        if selected_course_ids:
            request.session["selected_courses"] = selected_course_ids 
        return redirect("edu:dashboard")
    return redirect("edu:dashboard")
    
@login_required
def index(request):
    return render(request, "edu/index.html", {})

@login_required
def teachers(request):
    return render(request, "edu/teachers/teachers.html", {})

@login_required
def classSize(request):
    return render(request, "edu/teachers/class-size.html", {})

@login_required
def studentsAge(request):
    return render(request, "edu/teachers/students-age.html", {})

@login_required
def tools(request):
    courses = Course.objects.all() 
    return render(request, "edu/teachers/tools.html", {"courses": courses})

@login_required
def courses(request):
    courses = Course.objects.all() 
    return render(request, "edu/courses/index.html", {"courses": courses})

@login_required
def fetching(request):
    return render(request, "edu/teachers/fetching.html", {})

@login_required
def futureTeachers(request):
    return render(request, "edu/future-teachers/future-teachers.html", {})

@login_required
def dashboard(request):
    selected_course_ids = request.session.get("selected_courses", [])
    courses = Course.objects.filter(id__in=selected_course_ids) if selected_course_ids else []  
    students = StudentProfile.objects.filter(created_by=request.user)
    today = timezone.now().date()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request=request)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"✅ Student {user.first_name} {user.last_name} added successfully!")
            return redirect('edu:dashboard')
    else:
        form = CustomUserCreationForm(request=request)  

    return render(
        request, 
        "edu/teachers/dashboard.html", 
        {"courses": courses, "students": students, "today": today, "form": form}
    )

def addStudent(request):  
    if request.method == "POST":  
        form = CustomUserCreationForm(request.POST, request=request)
        if form.is_valid():  
            student = form.save(commit=False)  
            student.created_by = request.user 
            student.save() 
            return redirect('edu:dashboard') 
    return redirect('edu:dashboard')

def mark_attendance(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    today = timezone.now().date()
    if student.last_attended == today:
        messages.info(request, f"⚠️ Attendance already marked for {student.student.first_name} today.")
    else:
        student.mark_attendance()
        messages.success(request, f"✅ Attendance marked for {student.student.first_name} {student.student.last_name}!")
    return redirect('edu:dashboard')