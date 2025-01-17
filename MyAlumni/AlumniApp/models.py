from django.contrib.auth.models import AbstractUser
from django.db import models


USER_ROLES = [
    ('Admin', 'Admin'), 
    ('Alumni', 'Alumni'),
    ('Student', 'Student'),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=USER_ROLES, default='Student')