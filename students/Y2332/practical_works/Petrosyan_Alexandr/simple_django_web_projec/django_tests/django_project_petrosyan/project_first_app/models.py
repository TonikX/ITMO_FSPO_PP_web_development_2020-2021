from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


# Cars -------------------------------------------------------------------------

class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.number


class CarOwner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)
    cars = models.ManyToManyField(Car, through='Ownership')

    passport = models.CharField(max_length=10)
    address = models.TextField()
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.owner} - {self.car}"


class DriverLicense(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateTimeField


# Examples ---------------------------------------------------------------------

class ExampleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Publisher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.publisher}"
