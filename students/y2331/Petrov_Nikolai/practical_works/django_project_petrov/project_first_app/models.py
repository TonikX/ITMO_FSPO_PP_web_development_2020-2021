from django.db import models
from django.contrib.auth.models import AbstractUser
from django_project_petrov import settings


class Car(models.Model):
    car_id = models.IntegerField
    number_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.number_plate} {self.brand} {self.model} {self.color}'


class Owner(AbstractUser):
    cars = models.ManyToManyField(Car, through="Owning")
    birthday = models.DateTimeField

    passport = models.CharField(max_length=10, blank=True, null=True, default='')
    home_address = models.CharField(max_length=250, blank=True, null=True, default='')
    nationality = models.CharField(max_length=25, blank=True, null=True, default='')

    def __str__(self):
        return f'{self.username}:{self.password} {self.first_name} {self.last_name}'


class OwnerLicense(models.Model):
    license = models.IntegerField
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    start_date = models.DateTimeField


class Owning(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField
