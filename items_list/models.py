from collections.abc import Iterable
from django.db import models

from registration.models import UserModel
from locations.models import Country, Regions, Districts

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
    image = models.ImageField(upload_to='./imgs/items', null=True)
    name = models.CharField(max_length=25)

class Item(models.Model) :
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryLang, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, null=True)
    photos = models.ManyToManyField(PhotoItem, null=True)
    is_active = models.BooleanField()
    active_time = models.DateTimeField(null=True)
    title = models.CharField(max_length=15)
    price = models.FloatField()
    description = models.CharField(max_length=255)

class PartnerItem(models.Model):
    title = models.CharField(max_length=25)
    item = models.ManyToManyField(Item)