from django.db import models


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateTimeField()


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class DriverLicense(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number_id = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()


class Ownership(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()



