from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from blog.models import Post

class ProfileId(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobs = models.CharField(max_length=100,unique=True)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    git = models.URLField(blank=True)
    leetcode = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    bookmarked_posts = models.ManyToManyField(Post, related_name='bookmarked_by')

    def __str__(self):
        return self.jobs

class Career(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
