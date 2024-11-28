# courses/admin.py
from django.contrib import admin
from .models import Course, Certificate

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image')

admin.site.register(Certificate)