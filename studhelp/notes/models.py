from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Jobs(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    timeStamp =models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User , related_name="notes",blank=True)
    def __str__(self):
        return self.title

class Roadmap(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='roadmaps')
    step_title = models.CharField(max_length=200)
    article = models.URLField()
    desc = models.CharField(max_length=250)
    course = models.URLField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.job.title} - {self.step_title}"