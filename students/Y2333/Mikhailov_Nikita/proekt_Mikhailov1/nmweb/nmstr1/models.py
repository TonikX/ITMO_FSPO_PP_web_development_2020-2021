from django.db import models


# Create your models here.

class Car_owner(models.Model):
    idOwner = models.IntegerField()
    second_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    Birthday = models.DateField()

class Car(models.Model):
    id_car = models.IntegerField()
    government_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Possesion(models.Model):
    id_CarOwner = models.ForeignKey(Car_owner, default=1, on_delete=models.CASCADE)
    id_Car = models.ForeignKey(Car, default=1,  on_delete=models.CASCADE)
    Beginning_date = models.DateField()
    End_date = models.DateField()


class License(models.Model):
    id_license = models.IntegerField()
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()
