from django.db import models
from django.contrib.auth.models import AbstractUser
from django_project_Skopintsev import settings


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.state_number)


class CarOwner(AbstractUser):
    number_of_passport = models.BigIntegerField(null=True)
    address = models.CharField(max_length=135, null=True)
    nationality = models.CharField(max_length=15, null=True)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=True)
    cars = models.ManyToManyField(Car, through='OwnerShip')

    def __str__(self):
        return str(self.username)


class OwnerShip(models.Model):
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_number = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_sale = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


class DriverLicense(models.Model):
    owner_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

    def __str__(self):
        return str(self.number)
