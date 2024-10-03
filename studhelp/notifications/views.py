from django.shortcuts import render
from .models import Jobnotif
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

def job(request):
    jobnotif = Jobnotif.objects.order_by('-timeStamp')
    return render(request, 'notifications/job.html', {'jobnotif': jobnotif})
