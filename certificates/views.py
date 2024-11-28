import cv2
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import os
from .models import Certificate
import os

template_image = cv2.imread('static/images/template.png')

def update_certificate_template(template_image, user_name):
    template = template_image.copy()
    coords = (20,30) 
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    font_color = (0, 0, 0)  
    font_scale = 1
    thickness = 1
    line_type = cv2.LINE_AA
    cv2.putText(template, user_name, coords, font, font_scale, font_color, thickness, lineType=line_type)
    return template

def generate_certificate(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        updated_template = update_certificate_template(template_image, user_name)
        ret, buf = cv2.imencode('.png', updated_template)
        image = ContentFile(buf.tobytes())
        certificate = Certificate(user_name=user_name)
        certificate.certificate_image.save(f"{user_name}.png", image)
        certificate.save()
        return redirect('certificate_display', id=certificate.id)
    else:
        return render(request, 'certificates/form.html')

def certificate_display(request, id):
    certificate = Certificate.objects.get(id=id)
    return render(request, 'certificates/certificate.html', {'certificate': certificate})
