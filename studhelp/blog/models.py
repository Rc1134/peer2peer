from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=25)
    content=RichTextField(blank=True , null = True)
    slug = models.CharField(max_length=130)
    timeStamp =models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User , related_name="blogPost")
    def __str__(self):
        return self.title+"by"+self.author
    def total_likes(self):
        return self.likes.count()

class dcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , null=True)
    timeStamp =models.DateTimeField(auto_now_add=True)
    
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'content']
