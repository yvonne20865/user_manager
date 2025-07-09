from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('normal', 'Normal User'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    # Add more profile fields as needed
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='normal')
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
