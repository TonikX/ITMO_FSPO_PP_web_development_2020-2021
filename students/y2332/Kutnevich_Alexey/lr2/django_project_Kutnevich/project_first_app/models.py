from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    number = models.CharField(max_length=15)
    stump = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} {}".format(self.number, self.stump)


class CarOwner(models.Model):
    Second_name = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    Birth = models.DateField(null=True)
    cars = models.ManyToManyField(Car, through='Own')

    def __str__(self):
        return self.First_name, self.Second_name


class Own(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_of_start = models.DateField()
    date_of_end = models.DateField(null=True)


class DriveCard(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
