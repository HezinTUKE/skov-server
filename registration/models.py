from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.conf import settings  
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager 

class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True)
    email = models.EmailField(("email address"), unique=False)
    first_name = models.CharField(default= "", null=False)
    last_name = models.CharField(default= "", null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(blank=True, default=timezone.now, null=False)
    
    phone = models.CharField(max_length=13)
    date_of_birth = models.DateField(blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created :
        if instance.is_superuser:    
            Token.objects.create(user=instance, key="superuser_key")
        else:
            Token.objects.create(user=instance)
