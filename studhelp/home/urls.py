from django.contrib import admin
from django.urls import path, include
from home import views 
import blog 
from home.views import CustomPasswordChangeView

urlpatterns = [
     path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('admin/', admin.site.urls),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('careerpaths/', views.careerpaths, name='careerpaths'),
     path('settings/', views.settings_view, name='settings'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
]

