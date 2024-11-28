from django.db import models
from django.utils.text import slugify

class Certificate(models.Model):
    user_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates-created/')
    timestamp = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    from django.db import models