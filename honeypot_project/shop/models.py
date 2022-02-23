from unicodedata import name
from django.db import models
from django.http import HttpResponse


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = "static/images/")
    



# Create your models here.


