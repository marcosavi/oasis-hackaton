# Generated by Django 5.1.3 on 2025-01-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edu", "0005_rename_logo_course_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="video",
            field=models.FileField(blank=True, upload_to="videos/"),
        ),
    ]
