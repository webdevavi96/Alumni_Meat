from django.contrib import admin
from .models import User, BlogPosts

# Register your models here.

admin.site.register(User)
admin.site.register(BlogPosts)