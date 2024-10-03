# Generated by Django 5.0.6 on 2024-09-18 07:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('email', models.CharField(max_length=100)),
                ('Stream', models.CharField(choices=[('CSE', 'CSE'), ('AIML', 'AIML'), ('DS', 'DS'), ('CS', 'CS'), ('IOT', 'IOT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
