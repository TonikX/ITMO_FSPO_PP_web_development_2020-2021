from django.db import models


class Car_owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()


class Drivers_license(models.Model):
    owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    date_of_issue = models.DateField()


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    car_model = models.CharField(max_length=20)
    car_mark = models.CharField(max_length=20)
    car_color = models.CharField(max_length=30)


class Ownership(models.Model):
    owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_the_begin = models.DateField()
    date_of_the_end = models.DateField()
