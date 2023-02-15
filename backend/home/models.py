from django.conf import settings
from django.db import models
class Item(models.Model):
    'Generated Model'
    type = models.CharField(max_length=100,)
    availability = models.CharField(max_length=100,)
    price = models.IntegerField()
    location = models.CharField(max_length=100,)
class User(models.Model):
    'Generated Model'
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    phone = models.CharField(max_length=20,)
    email = models.EmailField(max_length=254,)
class Auth(models.Model):
    'Generated Model'
    uuid = models.UUIDField()
    email = models.EmailField(max_length=254,null=True,blank=True,)
    password = models.CharField(max_length=256,null=True,blank=True,)
