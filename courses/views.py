import cv2
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Certificate
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

#@login_required
def index(request):
    courses = Course.objects.all()
    return render(request, "courses/index.html", {'courses': courses})

def update_certificate_template(template_image, user_name, language):
    language_templates = {
        'en': 'static/images/template-en.png',
        'pt': 'static/images/template-pt.png',
    }

    template_path = language_templates.get(language, 'static/images/template-en.png')
    template_image = cv2.imread(template_path)
    if template_image is None:
        raise FileNotFoundError(f"Template not found at {template_path}")
    
    template = template_image.copy()
    image_height, image_width, _ = template.shape 

    base_font_scale = 1 
    font_scale = base_font_scale * (image_width / 1000) 
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_color = (0, 0, 0)
    thickness = 2
    line_type = cv2.LINE_AA

    text_size = cv2.getTextSize(user_name, font, font_scale, thickness)[0]
    text_width, text_height = text_size

    text_y_positions = {
        'en': 320,
        'pt': 630,
    }
    text_y = text_y_positions.get(language, 320)
    text_x = (image_width - text_width) // 2
    cv2.putText(template, user_name, (text_x, text_y), font, font_scale, font_color, thickness, lineType=line_type)
    return template

def course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        user_name = request.POST['user_name']
        language = request.POST['language']
        template_image = cv2.imread('static/images/template.png')
        updated_template = update_certificate_template(template_image, user_name, language)
        ret, buf = cv2.imencode('.png', updated_template)
        image = ContentFile(buf.tobytes())
        certificate = Certificate(user_name=user_name)
        certificate.certificate_image.save(f"{user_name}_{language}.png", image)
        certificate.save()
        return redirect('courses:conclusion', id=certificate.id)
    return render(request, 'courses/course.html', {'course': course})

def certificate_display(request, id):
    certificate = Certificate.objects.get(id=id)
    return render(request, 'courses/certificate.html', {'certificate': certificate})

def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:index')
    else:
        form = CourseForm()
    return render(request, 'courses/add.html', {'form': form})
