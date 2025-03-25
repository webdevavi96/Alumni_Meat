from django.db import models
from django.contrib.auth.hashers import make_password

#Create your models here.....

class User(models.Model): 
    USER_TYPES = [
        ('ADMIN', 'Admin'),
        ('ALUMNI', 'Alumni'),
        ('STUDENT', 'Student'),
    ]

    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('Passout', 'Passout'),
    ]

    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='usersData/', null=True, blank=True)
    user_Email = models.EmailField(max_length=200, unique=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPES)
    branch = models.CharField(max_length=100, null=True, blank=True)
    enrollment_Number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, null=True, blank=True)
    user_Password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Hash password before saving (only on creation)
        if not self.pk or self._state.adding:
            self.user_Password = make_password(self.user_Password)
        super().save(*args, **kwargs)
    
    def __str__(self): 
        return self.full_name
    
    
    
class BlogPost(models.Model): 
  blog_Name = models.CharField(max_length=500)
  blog_Details = models.CharField(max_length=1000)
  image = models.ImageField(upload_to='blog_posts', null=True, blank=True)
  
  def __str__(self):
    return self.blog_Name
  