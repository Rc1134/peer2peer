# Generated by Django 5.0.6 on 2024-09-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateField(),
        ),
    ]
