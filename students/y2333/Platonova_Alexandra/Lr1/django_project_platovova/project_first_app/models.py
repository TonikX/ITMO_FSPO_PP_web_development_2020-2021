from django.db import models


# Create your models here.
class Car(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bith_date = models.DateTimeField(blank=True)
    cars = models.ManyToManyField(Car, through='Own')



class Own(models.Model):
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField(blank=True)
    id_carOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Doc(models.Model):
    id_carOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    doc_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.CharField(max_length=10)
