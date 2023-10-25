from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    warranty_info = models.TextField()
