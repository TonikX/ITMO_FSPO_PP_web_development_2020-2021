from django.db import models


class CarOwner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthdate = models.DateTimeField


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)


class Own(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateTimeField
    date_end = models.DateTimeField


class DriverLicense(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_release = models.DateTimeField
