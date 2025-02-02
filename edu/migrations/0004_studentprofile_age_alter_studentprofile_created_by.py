# Generated by Django 5.1.3 on 2025-01-31 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edu", "0003_remove_studentprofile_age"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="studentprofile",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_students",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
