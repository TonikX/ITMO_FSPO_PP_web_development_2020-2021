from django.db import models

class carOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()

class car(models.Model):
    gov_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

class owning(models.Model):
    carOwnerId = models.ForeignKey(carOwner, on_delete=models.CASCADE)
    carId = models.ForeignKey(car, on_delete=models.CASCADE)
    date_of_start = models.DateTimeField()
    date_of_end = models.DateTimeField()

class licence(models.Model):
    carOwnerId = models.ForeignKey(carOwner, on_delete=models.CASCADE)
    licenceNum = models.CharField(max_length=10)
    licenceType = models.CharField(max_length=10)
    date_of_receiving = models.DateTimeField()
# Create your models here.
