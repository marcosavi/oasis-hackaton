import cv2
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Certificate
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

@login_required
def index(request):
    courses = Course.objects.all()
    return render(request, "courses/index.html", {'courses': courses})

template_image = cv2.imread('static/images/template.png')

def update_certificate_template(template_image, user_name):
    template = template_image.copy()
    coords = (325,320) 
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    font_color = (0, 0, 0)  
    font_scale = 1
    thickness = 1
    line_type = cv2.LINE_AA
    cv2.putText(template, user_name, coords, font, font_scale, font_color, thickness, lineType=line_type)
    return template

@login_required
def course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        user_name = request.POST['user_name']
        updated_template = update_certificate_template(template_image, user_name)
        ret, buf = cv2.imencode('.png', updated_template)
        image = ContentFile(buf.tobytes())
        certificate = Certificate(user_name=user_name)
        certificate.certificate_image.save(f"{user_name}.png", image)
        certificate.save()
        return redirect('courses:conclusion', id=certificate.id)
    return render(request, 'courses/course.html', {'course': course})

def certificate_display(request, id):
    certificate = Certificate.objects.get(id=id)
    return render(request, 'courses/certificate.html', {'certificate': certificate})

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
