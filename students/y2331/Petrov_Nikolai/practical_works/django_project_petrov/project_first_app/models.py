from django.db import models


class Car(models.Model):
    car_id = models.IntegerField
    number_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.number_plate} {self.brand} {self.model} {self.color}'


class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    cars = models.ManyToManyField(Car, through="Owning")
    birthday = models.DateTimeField

    def __str__(self):
        return f'{self.name} {self.surname}'


class OwnerLicense(models.Model):
    license_id = models.IntegerField
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    start_date = models.DateTimeField


class Owning(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField
