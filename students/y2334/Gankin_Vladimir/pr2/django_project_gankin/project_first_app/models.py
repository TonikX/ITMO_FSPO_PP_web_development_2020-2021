from django.db import models


# Create your models here.
class AutoOwner(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday_date = models.DateTimeField(null=True)


class Auto(models.Model):
    number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Owning(models.Model):
    auto_owner = models.ForeignKey(AutoOwner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True)


class DriverLicense(models.Model):
    auto_owner = models.ForeignKey(AutoOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date = models.DateTimeField(null=False)
