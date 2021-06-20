from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CarOwner(AbstractUser):
    id_car_owner = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)


class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    car_owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')


class Ownership(models.Model):
    id_ownership = models.AutoField(primary_key=True)
    id_car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)


class DriverLicense(models.Model):
    id_driver_license = models.AutoField(primary_key=True)
    id_car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()
