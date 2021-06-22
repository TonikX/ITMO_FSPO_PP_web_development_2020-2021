from django.db import models
from datetime import datetime


class Playground(models.Model):
    address = models.CharField(max_length=50)
    directorSurname = models.CharField(max_length=50)
    childrenPrice = models.FloatField()
    discountPrice = models.FloatField()
    adultPrice = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.directorSurname, self.address)


class Ride(models.Model):
    name = models.CharField(max_length=50)
    startDate = models.DateField(default=datetime.now())
    lifetime = models.BigIntegerField()
    basePrice = models.BigIntegerField()
    playground = models.ForeignKey('Playground', on_delete=models.CASCADE)

    db_constraints = {
        'price_rule': 'check (basePrice > 0)',
    }

    def __str__(self):
        return '%s' % self.name


class Usage(models.Model):
    day = models.DateField(default=datetime.now())
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE)
    childrenSales = models.BigIntegerField()
    discountSales = models.BigIntegerField()
    adultSales = models.BigIntegerField()

    def __str__(self):
        return '%s' % self.day
