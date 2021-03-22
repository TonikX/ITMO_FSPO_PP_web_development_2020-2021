from django.db import models


# Create your models here.


class Car(models.Model):
    gov_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    #owners = models.ManyToManyField(CarOwner, through="Own")


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through="Own")



class DriverLicense(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    receiving_date = models.DateField()


class Own(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
