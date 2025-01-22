from django.shortcuts import render

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

def ptsdCourse(request):
    return render(request, "edu/teachers/ptsd.html", {})

def fetching(request):
    return render(request, "edu/teachers/fetching.html", {})

def dashboard(request):
    return render(request, "edu/teachers/dashboard.html", {})

def futureTeachers(request):
    return render(request, "edu/future-teachers/future-teachers.html", {})

