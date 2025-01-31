from django.contrib.auth.models import User, Group  
from django import forms  
from django.contrib.auth.hashers import make_password
from .models import StudentProfile

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) 
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        first_name = user.first_name[:3].lower()
        last_name = user.last_name[:3].lower()

        user.username = f"{first_name}{last_name}"
        password = f"{first_name}{last_name}"
        user.password = make_password(password)

        if commit:
            user.save()
            student_group, created = Group.objects.get_or_create(name="Student")
            user.groups.add(student_group)
            if self.request:
                StudentProfile.objects.create(student=user, created_by=self.request.user)

        return user
