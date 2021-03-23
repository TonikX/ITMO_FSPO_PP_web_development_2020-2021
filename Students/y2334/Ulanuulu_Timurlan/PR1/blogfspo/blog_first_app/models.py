from django.db import models
class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)

class DriversLicense(models.Model):
    owner_driverslicense = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number_of_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

class car(models.Model):
    state_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

class possession(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(car, on_delete=models.CASCADE)
    date_of_start = models.DateField()
    date_of_end = models.DateField(null=True)


# Create your models here.
