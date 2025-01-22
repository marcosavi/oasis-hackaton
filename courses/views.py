from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.conf import settings
import os

def index(request):
    # Fetch all courses to display on the homepage
    return render(request, "courses/index.html", {})


def update_certificate_template(template_path, user_name, language):
    # Language-specific templates
    language_templates = {
        'en': 'static/images/template-en.png',
        'pt': 'static/images/template-pt.png',
    }

    # Fallback to English if language template is not found
    template_path = language_templates.get(language, 'static/images/template-en.png')
    
    try:
        # Load the template image
        template = Image.open(template_path).convert("RGBA")
    except FileNotFoundError:
        raise FileNotFoundError(f"Template not found at {template_path}")

    draw = ImageDraw.Draw(template)
    image_width, image_height = template.size

    # Define font and calculate size
    base_font_size = 36
    font_size = int(base_font_size * (image_width / 1000))
    font_path = "static/fonts/arial.ttf"  # Replace with the actual path to your TTF font
    font = ImageFont.truetype(font_path, font_size)

    # Use font.getbbox() to calculate text size
    text_bbox = font.getbbox(user_name)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Text position and alignment
    text_y_positions = {
        'en': 320,
        'pt': 630,
    }
    text_y = text_y_positions.get(language, 320)
    text_x = (image_width - text_width) // 2

    # Draw the user name on the certificate
    draw.text((text_x, text_y), user_name, font=font, fill=(0, 0, 0, 255))

    return template

def course(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        language = request.POST['language']
        template_path = 'static/images/template.png'
        updated_template = update_certificate_template(template_path, user_name, language)

        # Save the certificate to the media directory
        media_dir = os.path.join(settings.MEDIA_ROOT, 'certificates')
        os.makedirs(media_dir, exist_ok=True)
        certificate_filename = f"{user_name}_{language}.png"
        certificate_path = os.path.join(media_dir, certificate_filename)
        updated_template.save(certificate_path)

        # Pass the media URL for the certificate to the display page
        certificate_url = f"{settings.MEDIA_URL}certificates/{certificate_filename}"
        return render(request, 'courses/certificate.html', {
            'certificate': {
                'user_name': user_name,
                'certificate_image': {'url': certificate_url},
            }
        })

    return render(request, 'courses/course.html')

from django.http import FileResponse
import os
from django.conf import settings

def certificate_display(request, filename):
    # Construct the full path to the certificate file
    certificate_path = os.path.join(settings.MEDIA_ROOT, 'certificates', filename)

    # Check if the file exists
    if not os.path.exists(certificate_path):
        return HttpResponse("Certificate not found.", status=404)

    # Serve the certificate as a file response
    return FileResponse(open(certificate_path, 'rb'), content_type='image/png')