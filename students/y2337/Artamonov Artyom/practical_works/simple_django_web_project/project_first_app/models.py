from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import DateField

# Create your models here.
class Car(models.Model):
    gov_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20, blank=True, null=True)

    # owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)

class CarOwner(AbstractUser):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    passport_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=30, default='russian')
    cars = models.ManyToManyField(Car, through='CarOwnership')
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ['date_of_birth']

class CarOwnership(models.Model):
    id_owner = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    id_car = models.ForeignKey(Car, on_delete=CASCADE)
    date_of_start = models.DateField()
    date_of_end = models.DateField()

class DrivingLicense(models.Model):
    id_owner = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    license_number = models.CharField(max_length=10)
    date_of_issue = models.DateField(auto_now=True)

