from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.contrib.auth import get_user_model

class Owner(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(null=True, blank=True)
    passport_number = models.CharField(max_length=10)
    adress = models.CharField(max_length=150, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)

class DriveLicense(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_num = models.CharField(max_length=10)
    tipe = models.CharField(max_length=10)
    date = models.DateTimeField()

class Car(models.Model):
    #MARK = models.TextChoices('BMW', 'Mitsubishi', 'Lada')
    state_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)#, choices= MARK.choices)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True)
    owner = models.ManyToManyField(Owner, through='Ownership')

class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

