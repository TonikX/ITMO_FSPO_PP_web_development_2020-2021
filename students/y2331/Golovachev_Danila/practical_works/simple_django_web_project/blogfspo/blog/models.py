from django.db import models


class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateTimeField()


class Id_ow(models.Model):
    owner_Car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number_ID = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    date_issue = models.DateTimeField()


class Car(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    member = models.ManyToManyField(CarOwner, through='Possession')


class Possession(models.Model):
    carowner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_in = models.DateField()
    date_out = models.DateField()