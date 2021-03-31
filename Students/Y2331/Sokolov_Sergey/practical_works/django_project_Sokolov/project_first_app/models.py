from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)

    def __str__(self):
        return "{} {} {} {}".format(self.brand, self.model, self.colour, self.state_number)


class CarOwner(AbstractUser):
    cars = models.ManyToManyField(Car, through='Own')

    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    password = models.CharField(max_length=30, default='mypwrd')

    surname = models.CharField(max_length=30, blank=True, null=True)
    passport_number = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.CharField(max_length=40, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)


class Own(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    date_start = models.DateTimeField
    date_end = models.DateTimeField


class DriverLicense(models.Model):
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_release = models.DateTimeField
