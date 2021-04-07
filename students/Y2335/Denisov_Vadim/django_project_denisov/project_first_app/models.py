from django.db import models
from django.contrib.auth.models import AbstractUser

from django_project_denisov import settings


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    State_number = models.CharField(max_length=15)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.State_number)


class User(AbstractUser):
    birthdate = models.DateField(null=True)
    pass_num = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=30, null=True)
    cars = models.ManyToManyField(Car, through='Ownership')


class Ownership(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


class License(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()

    def __str__(self):
        return str(self.num)