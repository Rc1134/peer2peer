# Generated by Django 5.0.6 on 2024-06-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_roadmap_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]
