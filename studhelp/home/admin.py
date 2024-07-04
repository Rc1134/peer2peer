from django.contrib import admin
from .models import Contact , ProfileId , Career
admin.site.register((Contact,ProfileId))
admin.site.register(Career)

# Register your models here.
