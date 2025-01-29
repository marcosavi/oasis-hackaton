from django.contrib import admin
from .models import Course, Chapter, Quiz, Question, Alternative

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Alternative)



