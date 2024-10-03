from django.urls import path
from . import views

urlpatterns = [
    path('bookmarks/', views.view_bookmarks, name='view_bookmarks'),
    path('bookmark/<int:pk>/', views.bookmark_post, name='bookmark_post'), 
]
