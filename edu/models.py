from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Course(models.Model):
    image = models.ImageField(storage=FileSystemStorage, blank = True)
    title = models.CharField("Course  title", max_length=50, blank = False, null = False)
    description = models.CharField("Course description", max_length = 200, blank = False, null = False)
    def __str__(self):
        return f"Course {self.id} - {self.title}"
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField("Chapter  title", max_length=50, blank = False, null = False)
    content = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True)
    order = models.PositiveIntegerField()
    class Meta:
        ordering = ['order']
    def __str__(self):
        return f"Course {self.course.id} - Chapter {self.order} - {self.title}"

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.OneToOneField(Chapter, on_delete=models.CASCADE, related_name='quiz')
    def __str__(self):
        return f"Quiz for Course {self.chapter.course.id} Chapter {self.chapter.id}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    def __str__(self):
        return f"Course {self.quiz.chapter.course.id} - Chapter {self.quiz.chapter.id} - Question {self.id}"

class Alternative(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='alternatives')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.text}"
    
class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_students", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    def mark_attendance(self):
        self.created_at = datetime.datetime.now()
        self.save()

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - Last attended: {self.created_at}"