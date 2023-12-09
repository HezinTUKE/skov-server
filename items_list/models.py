from collections.abc import Iterable
from django.db import models
from django.utils import timezone

import os

from registration.models import UserModel
from locations.models import Country, Regions, Districts

def photo_path(instance, filename) :
    upload_to = './imgs/items'
    ext = os.path.splitext(filename)[-1]
    
    now = timezone.now()
    
    str_now = now.strftime("%Y%m%d_%H%M%S%f")[:-3]
    name = f"{str_now}{ext}"

    return os.path.join(upload_to, name)

class CategoryLang(models.Model):
    name_en = models.CharField(max_length=25)
    name_sk = models.CharField(max_length=25)
    name_cz = models.CharField(max_length=25)

class SubCategory(models.Model):
    category = models.ForeignKey(CategoryLang, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=25)
    name_sk = models.CharField(max_length=25)
    name_cz = models.CharField(max_length=25)

class PhotoItem(models.Model) :
    image = models.ImageField(upload_to = photo_path)

class Item(models.Model) :
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryLang, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, null=True)
    photos = models.ManyToManyField(PhotoItem)
    is_active = models.BooleanField()
    create_time = models.DateTimeField(null = True)
    active_time = models.DateTimeField()
    title = models.CharField(max_length=15)
    price = models.FloatField()
    description = models.CharField(max_length=255)

class PartnerItem(models.Model):
    title = models.CharField(max_length=25)
    item = models.ManyToManyField(Item)
    