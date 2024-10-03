from venv import logger
from django.shortcuts import render,HttpResponse,get_object_or_404
from home.models import User,Career,ProfileId
from django.contrib import messages
from blog.models import Post
import logging
from blog.models import Post
from notes.models import Jobs,Roadmap
from notifications.models import Jobnotif
def home(request):
    allJobs = Jobs.objects.order_by('-timeStamp')[:3]
    allPosts = Post.objects.order_by('-likes')[:3]
    newjobs = Jobnotif.objects.order_by('-timeStamp')[:3]
    context = {
        'allPosts': allPosts,
        'allJobs': allJobs,
        'newjobs':newjobs,
    }
    return render(request, "home/homepage.html", context)
def title(request):
    allJobs = Jobs.objects.order_by('-timeStamp')[:3]
    allPosts = Post.objects.order_by('-likes')[:3]
    newjobs = Jobnotif.objects.order_by('-timeStamp')[:3]
    context = {
        'allPosts': allPosts,
        'allJobs': allJobs,
        'newjobs':newjobs,
    }
    return render(request, "home/homepage.html", context)

def profile(request):
    return render(request,'home/profile.html')
def login(request):
    return render(request,'home/login.html')




def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        suggestions = request.POST.get('suggestions')
        description = request.POST.get('description')
        print(name,phone,email,suggestions,description)
        if not name or not phone or not email:
            messages.error(request, "Please fill out all required fields.")
        else:
            contact = User(name=name, phone=phone, email=email, suggestions=suggestions, description=description)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
    return render(request, 'home/contact.html')

