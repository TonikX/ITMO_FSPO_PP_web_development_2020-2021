from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CarOwner(AbstractUser):
    national_CO = (
        ('RU', 'Russian'),
        ('AZ', 'Azerbajan'),
        ('FR', 'France'),
        ('ENG', 'English'),
        ('USA', 'United states'),
    )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    number_pass = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    national = models.CharField(max_length=3, blank=True, null=True, choices=national_CO)


class Id_ow(models.Model):
    owner_Car = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_ID = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    date_issue = models.DateTimeField()


class Car(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Possession')


class Possession(models.Model):
    carowner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_in = models.DateField()
    date_out = models.DateField()