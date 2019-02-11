from django.contrib import admin
from .models import BlogPost, Mentee
# Register your models here.

my_model = [BlogPost, Mentee]
admin.site.register(my_model)

