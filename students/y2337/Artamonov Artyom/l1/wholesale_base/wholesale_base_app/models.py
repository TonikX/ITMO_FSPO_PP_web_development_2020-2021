from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)


class Seller(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)


class Delivery(models.Model):
    date = models.DateField()
    product_quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=CASCADE)
    seller = models.ForeignKey(Seller, on_delete=CASCADE)

