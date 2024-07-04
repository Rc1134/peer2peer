from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post
from home.models import ProfileId , Career
from notes.models import Jobs,Roadmap
from django.db.models import Q
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User

from django.db.models import Q

from .models import ProfileId  # Import the Profile model

from django.contrib.auth.decorators import login_required

def search(request):
    query = request.GET.get('query', '')
    if len(query) > 100:
        messages.warning(request, "Query too long")
        allPosts = Post.objects.none()
        allJobs = Roadmap.objects.none()
    else:
        allPosts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author__icontains=query))
        allJobs = Roadmap.objects.filter(Q(step_title__icontains=query) | Q(desc__icontains=query))
    params = {'allPosts': allPosts , 'query':query , "allJobs":allJobs}
    return render(request,'home/search.html' , params)

def careerpaths(request):
    allpaths = Career.objects.all()
    print(allpaths)
    return render(request,"home/resources.html",{"allpaths":allpaths})


def jobsearch(request):
    user_profile = None
    filtered_posts = []

    try:
        user_profile = ProfileId.objects.get(user=request.user)
    except ProfileId.DoesNotExist:
        pass

    allPosts = Post.objects.all()

    if request.method == "POST":
        job = request.POST.get('jobs')
        if not job:
            messages.error(request, "Please fill out all required fields.")
        elif user_profile:
            if job not in user_profile.jobs:
                if user_profile.jobs:
                    user_profile.jobs += ', ' + job
                else:
                    user_profile.jobs = job
                user_profile.save()
                messages.success(request, "You have added one skill.")
            else:
                messages.info(request, "This skill already exists.")
        else:  # Create a new profile for the user
            user_profile = ProfileId.objects.create(user=request.user, jobs=job)
            messages.success(request, "You have added your first skill.")

    if user_profile:
        user_skills = user_profile.jobs.split(', ')
        for skill in user_skills:
            filtered_posts.extend(allPosts.filter(content__icontains=skill))

        # Remove duplicates from filtered_posts
        filtered_posts = list(set(filtered_posts))

    context = {'user_skills': user_profile.jobs.split(', ') if user_profile and user_profile.jobs else [],
               'filtered_posts': filtered_posts}
    return render(request, 'home/profile.html', context)


#Authentication APIs

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email2')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'home/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout succesful')
        return redirect('home')
    else:
        return render(request, 'home/login.html')