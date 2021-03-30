from django.db import models


class CarOwner(models.Model):
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    birthDate = models.DateField(null=True)


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class OwnerShip(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True, related_name='topic_owner_id')
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='topic_car_id')
    date_a = models.DateField()
    date_b = models.DateField(null=True)


class License(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()
