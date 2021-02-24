from django.db import models

class car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

class owner(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField()

class license(models.Model):
    owner_license = models.ForeignKey(owner,on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateTimeField()

class ownership(models.Model):
    owner_ownership = models.ForeignKey(owner,on_delete=models.CASCADE)
    car_ownership = models.ForeignKey(car,on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_ending = models.DateTimeField()

# Create your models here.
