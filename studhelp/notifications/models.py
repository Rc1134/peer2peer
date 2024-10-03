from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

class Jobnotif(models.Model):
    sno = models.AutoField(primary_key=True)
    jobtitle = models.CharField(max_length=250)
    requirements = RichTextField(blank=True , null = True)
    salary = models.CharField(max_length=250)
    link = models.URLField()
    slug = models.SlugField(max_length=130, unique=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    applicants = models.ManyToManyField(User,related_name='applied_jobs',blank=True)

    def __str__(self):
        return self.jobtitle

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.jobtitle)
        super().save(*args, **kwargs)
    
def send_new_job_email(sender, instance, created, **kwargs):
    if created: 
        subject = f"New Job Posted: {instance.jobtitle}"
        message = f"A new job has been posted on the site.\n\nTitle: {instance.jobtitle}\nSalary: {instance.salary}\nDetails: {instance.link}\n\nCheck it out!"
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email for user in User.objects.all() if user.email]
        send_mail(subject, message, email_from, recipient_list)