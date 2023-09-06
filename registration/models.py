from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class UserModel(User):
    phone = models.CharField(max_length=13)
    date_of_birth = models.DateField(blank=True, default='', null=False)