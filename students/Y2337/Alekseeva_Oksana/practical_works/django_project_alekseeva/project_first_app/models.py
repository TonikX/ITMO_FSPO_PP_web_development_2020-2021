from django.db import models

# Create your models here.

class Car_owner(models.Model):
    surname = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    date_of_birth = models.DateField()

class Car(models.Model):
    gos_number = models.CharField(max_length = 15)
    brand = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    color = models.CharField(max_length = 30, blank = True, null = True)

class Ownership(models.Model):
    id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null = True)

class Driving_license(models.Model):
    id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
    license_number = models.CharField(max_length = 10)
    type = models.CharField(max_length = 10)
    date_of_issue = models.DateField()
