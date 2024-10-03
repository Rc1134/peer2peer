from django.shortcuts import render,HttpResponse,redirect
from notes.models import Jobs
from django.db.models import Q
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect , get_object_or_404 , redirect 
from venv import logger
from django.shortcuts import render, HttpResponseRedirect , get_object_or_404 , redirect 
import logging
from blog.models import Post , dcomment , PostForm
from django.contrib import messages
from django.utils.text import slugify
from blog.templatetags import extras
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator


def jobnotes(request):
    alljobs = Jobs.objects.order_by('-timeStamp')
    context = {"alljobs":alljobs}
    return render(request, "notes/resources.html",context)

    
def roadmap_page(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    roadmap = job.roadmaps.order_by('order')
    return render(request, 'notes/topic_detail.html', {'job': job, 'likes_count':job.likes.count() ,'roadmap': roadmap})

def like_roadmap(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    if job.likes.filter(id=request.user.id).exists():
        job.likes.remove(request.user)
    else:
        job.likes.add(request.user)
    return HttpResponseRedirect(reverse('roadmap_page', args=[job.sno]))

