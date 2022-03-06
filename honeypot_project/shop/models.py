from unicodedata import name
from django.db import models
from django.http import HttpResponse


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = "static/images/")


class Comment(models.Model):
    product = models.CharField(max_length=30)
    poster = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    comment = models.CharField(max_length=250)
    



# Create your models here.


