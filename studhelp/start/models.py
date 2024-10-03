from django.db import models
from django.contrib.auth.models import User
class Account(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    rollnumber = models.CharField(max_length=13)
    phone=models.CharField(max_length=13)
    birthday = models.DateField()
    gender = models.CharField(max_length=6,choices=[('Male','Male'),('Female','Female')])
    email=models.CharField(max_length=100)
    Stream=models.CharField(max_length=6,choices=[('CSE','CSE'),('AIML','AIML'),('DS','DS'),('CS','CS'),('IOT','IOT'),('ECE','ECE'),('EEE','EEE'),('MECH','MECH'),('CIVIL','CIVIL')])
    def __str__(self):
        return self.user.username
