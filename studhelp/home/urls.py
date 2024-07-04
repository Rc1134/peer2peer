from django.contrib import admin
from django.urls import path,include
from home import views
import blog

urlpatterns = [
path('search/', views.search, name="search"),
path('login/', views.login_view , name = "login_view"),
path('logout', views.logout_view , name = "logout_view"),
path('jobsearch/', views.jobsearch , name = "jobsearch"),
path('careerpaths/',views.careerpaths,name="careerpaths"),
]


