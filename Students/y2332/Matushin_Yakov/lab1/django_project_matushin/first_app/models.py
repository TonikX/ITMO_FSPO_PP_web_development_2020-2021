from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()


class License(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Auto(models.Model):
    number = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class AutoOwner(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

# Create your models here.
