from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.


class Car(models.Model):
    COLORS = (
        (1, 'Black'),
        (2, 'White'),
        (3, 'Blue'),
        (4, 'Grey'),
        (5, 'Yellow'),
        (6, 'Green'),
        (7, 'Red'),
    )
    gov_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=30, choices=COLORS)
    # owners = models.ManyToManyField(CarOwner, through="Own")


class CarOwner(AbstractUser):
    # first_name = models.CharField(max_length=30, blank=True, null=True)
    # last_name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    passport_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    cars = models.ManyToManyField(Car, through="Own", blank=True, null=True)


# CarOwner = get_user_model()


class DriverLicense(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    receiving_date = models.DateField()


class Own(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
