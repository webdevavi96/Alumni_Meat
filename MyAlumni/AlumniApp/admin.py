from django.contrib import admin
from .models import Users, BlogPosts

# Register your models here.

admin.site.register(Users)
admin.site.register(BlogPosts)