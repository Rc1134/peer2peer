# Generated by Django 5.0.6 on 2024-09-05 15:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_jobs_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
