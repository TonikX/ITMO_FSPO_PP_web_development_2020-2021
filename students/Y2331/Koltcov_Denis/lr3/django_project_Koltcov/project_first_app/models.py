from django.db import models
from django import forms


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.number}"


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class License(models.Model):
    TYPE_LS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
         )
    type = models.CharField(blank=True, choices=TYPE_LS, max_length=1)
    number = models.CharField(max_length=10)
    issue_date = models.DateField()
    ownerId = models.ForeignKey(CarOwner, on_delete=models.CASCADE)


class Ownership(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    ownerId = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    carId = models.ForeignKey(Car, on_delete=models.CASCADE)





