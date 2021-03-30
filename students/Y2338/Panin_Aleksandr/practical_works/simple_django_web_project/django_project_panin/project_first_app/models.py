from django.db import models


class CarOwner(models.Model):
    id_car_owner = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField(null=True)


class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    car_owners = models.ManyToManyField(CarOwner, through='Ownership')


class Ownership(models.Model):
    id_ownership = models.AutoField(primary_key=True)
    id_car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)


class DriverLicense(models.Model):
    id_driver_license = models.AutoField(primary_key=True)
    id_car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()
