from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class Owner(AbstractUser):
    #username = models.CharField(max_length=20, unique=True)
    #password = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class DriversLicense(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()

    def __str__(self):
        return f'{self.license_number}'


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.brand}, {self.license_plate}'


class CarOwner(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.owner_id}, {self.car_id}'
