from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Car(models.Model):
    gos_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

    def Car(self):
        return self.gos_number, self.brand, self.model, self.colour


class Car_owner(AbstractUser):
    surname = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    connection = models.ManyToManyField(Car, through="Ownership", blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    home_address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=15, blank=True, null=True)


class Ownership(models.Model):
    id_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class Driving_license(models.Model):
    id_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()
