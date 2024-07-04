from django.shortcuts import render,HttpResponse,redirect
from notes.models import Jobs
from django.db.models import Q
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def jobnotes(request):
    alljobs = Jobs.objects.all()
    context = {"alljobs":alljobs}
    return render(request, "notes/resources.html",context)
    
def roadmap_page(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    roadmap = job.roadmaps.order_by('order')
    return render(request, 'notes/topic_detail.html', {'job': job, 'roadmap': roadmap})