from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.brand} {self.model} {self.car_number}"


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(blank=True, null=True)
    car = models.ManyToManyField(Car, through='Owning')
    passport_num = models.CharField(max_length=50, blank=True, null=True, default="passport number")
    nationality = models.CharField(max_length=50, blank=True, null=True, default="nationality")
    address = models.TextField(blank=True, null=True, default="address")
    

class License(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
class Owning(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

