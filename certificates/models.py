from django.db import models

# Create your models here.
class Certificate(models.Model):
    user_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates-created/')
    timestamp = models.DateTimeField(auto_now_add=True)