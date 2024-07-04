from django.contrib import admin
from blog.models import Post , dcomment
admin.site.register((Post,dcomment))