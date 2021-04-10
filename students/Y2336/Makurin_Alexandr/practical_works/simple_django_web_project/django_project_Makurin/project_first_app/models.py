from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class CarOwner(models.Model):
#     Surname = models.CharField(max_length=30)
#     Name = models.CharField(max_length=30)
#     BirthDate = models.DateTimeField()
#
#     def __str__(self):
#         return f"{self.Name} {self.Surname}"


# Create your models here.
class User(AbstractUser):
    PassportNumber = models.BigIntegerField(unique=True)
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    BirthDate = models.DateTimeField()
    Address = models.TextField()
    Nationality = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Name} {self.Surname}"


class DriversLicense(models.Model):
    OwnerId = models.ForeignKey(User, on_delete=models.CASCADE)
    LicenseNumber = models.CharField(max_length=10)
    Type = models.CharField(max_length=10)
    DateOfIssue = models.DateTimeField()


class Car(models.Model):
    GosNum = models.CharField(max_length=15, unique=True)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.Brand} {self.Model}"


class Owning(models.Model):
    OwnerId = models.ForeignKey(User, on_delete=models.CASCADE)
    CarId = models.ForeignKey(Car, on_delete=models.CASCADE)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
