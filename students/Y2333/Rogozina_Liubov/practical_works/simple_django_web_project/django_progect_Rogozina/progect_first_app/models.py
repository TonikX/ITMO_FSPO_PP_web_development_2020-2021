from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Car_owner(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True, default="Hello")
    passport = models.BigIntegerField(blank=True, null=True)
    home_address = models.CharField(max_length=150, blank=True, null=True)
    nacional = models.CharField(max_length=20, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    def __str__(self):
         return self.last_name + " " +self.first_name

    REQUIRED_FIELDS = ['first_name', 'last_name']

class Driver_license(models.Model):
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    date_give = models.DateTimeField()
    def __str__(self):
        return self.license_number;
class Car(models.Model):
    license_number=models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')
    def __str__(self):
        return self.car_model + " "+ self.license_number;
class Ownership(models.Model):
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()