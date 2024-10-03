from django.contrib import admin
from django.urls import path,include
from notes import views
import blog

urlpatterns = [
path('jobnotes/',views.jobnotes,name="jobnotes"),
path('jobnotes/<int:job_id>/', views.roadmap_page, name='roadmap_page'),
path('jobnotes/<int:job_id>/like/', views.like_roadmap, name='like_roadmap'),
]


