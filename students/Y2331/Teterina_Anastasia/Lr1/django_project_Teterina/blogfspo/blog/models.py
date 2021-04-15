from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


class Owner(AbstractUser):
    NAT_CO = (
        ('RU', 'Russian'),
        ('BR', 'Belarus'),
        ('UK', 'Ukraine'),
        ('TAT', 'Tatarstan'),
        ('BA', 'Bashkorstan'),
        ('ARM', 'Armenia')
    )
    owner_id = models.IntegerField(null = True)
    last_name = models.CharField(max_length=30, null = True)
    name = models.CharField(max_length=30, null = True)
    date_birth = models.DateField(null = True)
    passport = models.CharField(max_length=10, blank=True, null = True)
    address = models.CharField(max_length=100, blank=True, null = True)
    national = models.CharField(max_length=50, blank=True, null = True, choices=NAT_CO)


class Car(models.Model):
    car_id = models.IntegerField()
    gov_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)


class Ownering(models.Model):
    car_owner_id = models.IntegerField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class Driver_license(models.Model):
    driver_lic_id = models.IntegerField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number_lic = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()
