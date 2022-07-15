from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')


class Foodshelf(models.Model):
    food_name = models.CharField(max_length=200)
    expiry_date = models.IntegerField(default=0)
    food_status = models.CharField(max_length=200)
    liter_kilogram = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
