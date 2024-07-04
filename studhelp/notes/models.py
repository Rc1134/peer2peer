from django.db import models

class Jobs(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    
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