from django.db import models


class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateTimeField


class OwnerLicense(models.Model):
    license_id = models.IntegerField
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    start_date = models.DateTimeField


class Car(models.Model):
    car_id = models.IntegerField
    number_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Owning(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField
