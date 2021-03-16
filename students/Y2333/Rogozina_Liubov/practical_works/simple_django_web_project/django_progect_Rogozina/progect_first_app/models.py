from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Car_owner(models.Model):
    surname = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    date_birth = models.DateField()
    def __str__(self):
        return self.surname + " " +self.name;
class Driver_license(models.Model):
    car_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    date_give = models.DateTimeField()
    def __str__(self):
        return self.license_number;
class Car(models.Model):
    license_number=models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(Car_owner, through='Ownership')
    def __str__(self):
        return self.car_model + " "+ self.license_number;
class Ownership(models.Model):
    car_owner = models.ForeignKey(Car_owner,on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()