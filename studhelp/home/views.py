from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post
from home.models import ProfileId , Career
from notes.models import Jobs,Roadmap
from django.db.models import Q
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from notifications.models import Jobnotif
from start.models import Account

from django.db.models import Q



def search(request):
    query = request.GET.get('query', '')
    
    if not query:  # Check if the query is empty
        allPosts = Post.objects.none()
        allJobs = Roadmap.objects.none()
        allRoadmaps = Jobs.objects.none()
        newJobs = Jobnotif.objects.none()
        users = User.objects.none()
    elif len(query) > 100:
        messages.warning(request, "Query too long")
        allPosts = Post.objects.none()
        allJobs = Roadmap.objects.none()
        allRoadmaps = Jobs.objects.none()
        newJobs = Jobnotif.objects.none()
        users = User.objects.none()
    else:
        allPosts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        allJobs = Roadmap.objects.filter(Q(step_title__icontains=query) | Q(desc__icontains=query))
        allRoadmaps = Jobs.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
        newJobs = Jobnotif.objects.filter(Q(jobtitle__icontains=query) | Q(requirements__icontains=query))
        users = Account.objects.filter(rollnumber=query)
        
        if users.exists():
            user_profile = users.first()
            return redirect('profile_view', user_id=user_profile.user.id)
    
    params = {
        'allPosts': allPosts,
        'query': query,
        'allJobs': allJobs,
        'allRoadmaps': allRoadmaps,
        'newJobs': newJobs,
        'users': users
    }
    return render(request, 'home/search.html', params)



def careerpaths(request):
    allpaths = Career.objects.all()
    print(allpaths)
    return render(request,"home/resources.html",{"allpaths":allpaths})

def myprofile(request):
    user_profile = None
    filtered_posts = []
    filtered_jobs = []
    user = request.user

    if not user.is_authenticated:
        return redirect('login_view') 

    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        account = None

    user_profile, created = ProfileId.objects.get_or_create(user=user)

    if request.method == "POST":
        job = request.POST.get('jobs')
        action = request.POST.get('action')

        if action == 'submit':
            if not job:
                messages.error(request, "Please fill out all required fields.")
            else:
                jobs_list = user_profile.jobs.split(', ') if user_profile.jobs else []
                if job not in jobs_list:
                    jobs_list.append(job)
                    user_profile.jobs = ', '.join(jobs_list)
                    user_profile.save()
                    messages.success(request, "You have added a new skill.")
                else:
                    messages.info(request, "This skill already exists.")
        
        elif action == 'load':
            if user_profile and user_profile.jobs:
                user_skills = user_profile.jobs.split(', ')
                if user_skills:
                    query = Q()
                    for skill in user_skills:
                        query |= Q(content__icontains=skill)
                    filtered_posts = Post.objects.filter(query).distinct().order_by('-timeStamp')[:2]
                    
                    job_query = Q()
                    for skill in user_skills:
                        job_query |= Q(requirements__icontains=skill)
                    filtered_jobs = Jobnotif.objects.filter(job_query).distinct().order_by('-timeStamp')[:4]
            else:
                messages.info(request, "No skills found to load posts.")
                
    context = {
        'account': account,
        'user_profile': user_profile,
        'user_skills': user_profile.jobs.split(', ') if user_profile and user_profile.jobs else [],
        'filtered_posts': filtered_posts,
        'filtered_jobs': filtered_jobs
    }
    return render(request, 'home/profile.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    # Capture the next parameter from both GET and POST methods
    next_page = request.GET.get('next') or request.POST.get('next')

    if request.method == 'POST':
        email = request.POST.get('email2')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            # Redirect to the captured next page if available; otherwise, go to 'home'
            return redirect(next_page if next_page else 'home')
        else:
            messages.warning(request, 'Invalid credentials')
            # Pass the next parameter back to the login page
            return redirect(f"{request.path}?next={next_page}")
    
    # Render the login page for GET requests
    return render(request, 'home/login.html', {'next': next_page})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout succesful')
        return redirect('home')
    else:
        return render(request, 'home/homepage.html')

def home(request):
    allJobs = Jobs.objects.all()
    allPosts = Post.objects.all()

    context = {
        'allPosts': allPosts,
        'allJobs': allJobs,
    }
    return render(request, "home/homepage.html", context)
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordChangeView

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'home/password_change_form.html'
    success_url = '/password_change/'  

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your password has been changed successfully.")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "There was an error changing your password. Please try again.")
        return response

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import ProfileId

@login_required
def settings_view(request):
    user_profile, created = ProfileId.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('settings')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'home/settings.html', {'user_profile':user_profile,'form': form})


from django.shortcuts import render, get_object_or_404

def profile_view(request, user_id):
    profile = get_object_or_404(ProfileId, user_id=user_id)
    account = get_object_or_404(Account, user_id=user_id)
    user_profile = get_object_or_404(ProfileId, user_id=user_id)
    user_skills = user_profile.jobs.split(', ') if user_profile.jobs else [] 
    posts = Post.objects.filter(author_id=user_id).order_by('-timeStamp') # Get all posts by this user

    return render(request, 'home/profile_detail.html', {
        'profile': profile,
        'account': account,
        'user_skills': user_skills,
        'posts': posts,
    })