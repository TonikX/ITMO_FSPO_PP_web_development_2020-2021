from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class car(models.Model):
    gov_number = models.CharField(max_length = 15)
    brand = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    color = models.CharField(max_length = 30)

class owner(AbstractUser):
    last_name = models.CharField(max_length = 30, blank = True, null = True)
    name = models.CharField(max_length = 30, blank = True, null = True)
    borndate = models.DateTimeField(blank = True, null = True)
    passNumber = models.CharField(max_length = 16, blank = True, null = True)
    address = models.CharField(max_length = 30, blank = True, null = True)
    nationality = models.CharField(max_length = 15, blank = True, null = True)
    cars = models.ManyToManyField(car, through = "owning")

class card(models.Model):
    owner_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    card_number = models.CharField(max_length = 10)
    type = models.CharField(max_length = 10)
    getdate = models.DateTimeField()

class owning(models.Model):
    owner_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    car_ID = models.ForeignKey(car, on_delete = models.CASCADE)
    begin = models.DateTimeField()
    end = models.DateTimeField() 
