from django.db import models


# Create your models here.
class CarOwner(models.Model):
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    BirthDate = models.DateTimeField()


class DriversLicense(models.Model):
    OwnerId = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    LicenseNumber = models.CharField(max_length=10)
    Type = models.CharField(max_length=10)
    DateOfIssue = models.DateTimeField()


class Car(models.Model):
    GosNum = models.CharField(max_length=15)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=30, null=True)


class Owning(models.Model):
    OwnerId = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    CarId = models.ForeignKey(Car, on_delete=models.CASCADE)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
