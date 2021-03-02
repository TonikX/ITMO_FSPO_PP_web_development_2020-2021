from django.db import models


# Create your models here.
class CarOwner(models.Model):
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Bday = models.DateField()


class DriverLicense(models.Model):
    IdOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    IdNumber = models.CharField(max_length=10)
    Type = models.CharField(max_length=10)
    DateOfIssue = models.DateField(null=False)


class Car(models.Model):
    GovernmentNumber = models.CharField(max_length=15)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    IdCarOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    IdCar = models.ForeignKey(Car, on_delete=models.CASCADE)
    Start = models.DateField(null=False)
    End = models.DateField()