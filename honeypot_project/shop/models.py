from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = "static/images/")

# Create your models here.
