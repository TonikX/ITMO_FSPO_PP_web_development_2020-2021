from django.db import models

class  CarOwner (models.Model):
    Surname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Birthdate = models.DateField(null=True)

class Car(models.Model):

    State_number = models.CharField(max_length=20)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Colour = models.CharField(max_length=30, null=True)
    models.ManyToManyField(CarOwner, through='Owership')


class Ownership(models.Model):
    ID_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    ID_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    Start_date = models.DateField()
    End_date = models.DateField(null=True)


class DrivingLicense(models.Model):
    ID_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    Number_id_card = models.CharField(max_length=10)
    Type = models.CharField(max_length=10)
    Date_of_issue = models.DateField()


