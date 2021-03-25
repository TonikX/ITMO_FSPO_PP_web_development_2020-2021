from django.db import models


class Owner(models.Model):
    owner_id = models.IntegerField()
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_birth = models.DateField()


class Car(models.Model):
    car_id = models.IntegerField()
    gov_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)
    owners = models.ManyToManyField(Owner, through='Owning')


class Owning(models.Model):
    car_owner_id = models.IntegerField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class Driver_license(models.Model):
    driver_lic_id = models.IntegerField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number_lic = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()
