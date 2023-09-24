from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=15)
    phone_code = models.CharField(max_length=10)
    short = models.CharField(max_length=5)

class Regions(models.Model):
    coutry = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.CharField(max_length=20)

class Districts(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    district = models.CharField(max_length=20)