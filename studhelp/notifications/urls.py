from django.contrib import admin
from django.urls import path,include
from notifications import views

urlpatterns = [
path('jobnotifications/',views.job,name="jobnotifications"),
]