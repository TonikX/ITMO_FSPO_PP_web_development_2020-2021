from django.db import models

class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()

class Car(models.Model):
    state_number = models.IntegerField()
    id_owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE, null=True)
    Brand = models.CharField(max_length=20, null=True)
    Model = models.CharField(max_length=20, null=True)
    Colour = models.CharField(max_length=30, null=True)

class OwnerShip(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete= models.CASCADE, null=True)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField(null=True)


class DrivingLicense(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    license_num = models.CharField(max_length=50)
    type=models.CharField(max_length=10)
    date_of_issue = models.DateTimeField(auto_now=True)

