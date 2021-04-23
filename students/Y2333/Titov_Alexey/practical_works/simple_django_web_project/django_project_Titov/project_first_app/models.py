from django.db import models

# Create your models here.


class Car(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "{} {} {} {}".format(self.gos_number, self.color, self.mark, self.model)

class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(blank=True, null=True)
    cars = models.ManyToManyField(Car, through='CarOwning')


class CarOwning(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)


class DriverLicense(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()
