from django.db import models


# Create your models here.
class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class possession(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)


class driverID(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField(blank=True, null=True)
