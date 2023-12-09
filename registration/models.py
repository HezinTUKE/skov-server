from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager 

class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True)
    email = models.EmailField(("email address"), unique=True)
    first_name = models.CharField(default= "", null=False)
    last_name = models.CharField(default= "", null=False)
    is_staff = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(blank=True, default=timezone.now, null=False)
    
    phone = models.CharField(max_length=13)
    date_of_birth = models.DateField(blank=True, null=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email