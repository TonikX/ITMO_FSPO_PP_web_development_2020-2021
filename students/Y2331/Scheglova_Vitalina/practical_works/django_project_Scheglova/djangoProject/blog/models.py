from django.db import models

class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateField


class Drivers_license(models.Model):
    owner_drivers_license = models.ForeignKey(Owner,on_delete=models.CASCADE)
    number_of_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField


class Car(models.Model):
    State_number = models.CharField(max_length=15)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=30)

class Possession(models.Model):
    owner_possession = models.ForeignKey(Owner, on_delete=models.CASCADE)
    the_date_of_the_beginning = models.DateField
    expiration_date = models.DateField
    car_possession = models.ForeignKey(Car, on_delete=models.CASCADE)