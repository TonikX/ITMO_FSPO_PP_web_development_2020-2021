from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    REQUIRED_FIELDS = []
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)
    passport_number = models.IntegerField(max_length=6, default='000000')
    home_address = models.CharField(max_length=100, default='Mars', null=True)
    nationality = models.CharField(max_length=30, default='Reptiloed', null=True)
    car = models.ManyToManyField('Car', through='Ownership')

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.first_name, self.last_name, self.birth_date, self.passport_number, self.home_address, self.nationality)

class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.number

class Ownership(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField(null=True)

class DriverLicense(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateTimeField
