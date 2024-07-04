from venv import logger
from django.shortcuts import render,HttpResponse,get_object_or_404
from home.models import Contact
from django.contrib import messages
from blog.models import Post
import logging
def home(request):
    return render(request,'home/home.html')
def title(request):
    return render(request,'home/home.html')

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
            contact = Contact(name=name, phone=phone, email=email, suggestions=suggestions, description=description)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
    return render(request, 'home/contact.html')

