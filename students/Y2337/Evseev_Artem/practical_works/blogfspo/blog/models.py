from django.db import models

# Create your models here.


class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

class License(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    
class Owning(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

