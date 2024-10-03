from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content=RichTextField(blank=True , null = True)
    image = models.ImageField(upload_to='comments/images/', null=True, blank=True)
    file = models.FileField(upload_to='comments/files/', null=True, blank=True)
    slug = models.CharField(max_length=130)
    timeStamp =models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="blogPost",blank=True)
    bookmark = models.ManyToManyField(User,related_name="bookmarked_posts",blank=True)
    def __str__(self):
        return self.title+"by"+str(self.author)
    def total_likes(self):
        return self.likes.count()
    def total_bookmarks(self):
        return self.bookmark.count()

class dcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , null=True)
    timeStamp =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comments/images/', null=True, blank=True)
    file = models.FileField(upload_to='comments/files/', null=True, blank=True)
    def comments_count(self):
        return self.comment.count()
    
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'content']
