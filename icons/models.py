from django.db import models
from django.utils import timezone

import os

def icon_path(instance, filename) :
    upload_to = './imgs/icons'
    ext = os.path.splitext(filename)[-1]
    
    now = timezone.now()
    
    str_now = now.strftime("%Y%m%d_%H%M%S%f")[:-3]
    name = f"{str_now}{ext}"

    return os.path.join(upload_to, name)

class Icon(models.Model):
    icon = models.ImageField(upload_to=icon_path)
    name = models.CharField(max_length=25, null = True)
    