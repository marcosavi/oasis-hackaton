# Generated by Django 5.1.3 on 2025-01-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edu", "0004_studentprofile_age_alter_studentprofile_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentprofile",
            name="age",
        ),
        migrations.AddField(
            model_name="studentprofile",
            name="last_attended",
            field=models.DateField(blank=True, null=True),
        ),
    ]
