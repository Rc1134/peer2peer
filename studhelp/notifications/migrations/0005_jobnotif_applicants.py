# Generated by Django 5.0.6 on 2024-09-13 09:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_jobnotif_salary'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='jobnotif',
            name='applicants',
            field=models.ManyToManyField(related_name='applied_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
