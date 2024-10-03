
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.blogHome , name = "blogHome"),
    path('postComment/', views.postComment, name='postComment'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('<slug:slug>/', views.blogPost, name='blogpost'),
    
]