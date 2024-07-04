from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    suggestions=models.CharField(max_length=500)
    description=models.CharField(max_length=600)
    def __str__(self):
        return "message from"+self.name+"-"+self.email

class ProfileId(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobs=models.CharField(max_length=100)
    def __str__(self):
        return self.jobs

class Career(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
