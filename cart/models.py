from django.db import models

class Products(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    detail = models.CharField(max_length=200)
    price = models.IntegerField()
    