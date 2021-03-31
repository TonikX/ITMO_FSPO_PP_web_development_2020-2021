from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    passport_number = models.IntegerField(max_length=10, null=True, blank=True)
    home_address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    cars = models.ManyToManyField('Car', through='Ownership')


class Car(models.Model):
    state_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=30, null=False)
    color = models.CharField(max_length=20, null=True)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Ownership(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)


class License(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    issue_date = models.DateField(null=False)
