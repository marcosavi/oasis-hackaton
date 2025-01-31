from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course, Chapter, Quiz, Question, Alternative, StudentProfile, Resources

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Alternative)
admin.site.register(StudentProfile)
admin.site.register(Resources)