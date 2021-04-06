from django.db import models


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.id)


class CarOwner(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    cars = models.ManyToManyField(Car, through='OwnerShip')

    def __str__(self):
        return str(self.id)


class OwnerShip(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_sale = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


class DriverLicense(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

    def __str__(self):
        return str(self.id)
