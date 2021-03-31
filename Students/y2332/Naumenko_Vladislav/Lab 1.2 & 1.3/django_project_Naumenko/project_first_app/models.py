from django.db import models


# Create your models here.

class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.pk}, {self.last_name}, {self.first_name}, {self.birth_date}'


class DriversLicense(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()

    def __str__(self):
        return f'{self.pk}, {self.owner_id}, {self.license_number}, {self.type}, {self.date_issue}'


class Auto(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.pk}, {self.license_plate}, {self.brand}, {self.model}, {self.color}'


class AutoOwner(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto_id = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.pk}, {self.owner_id}, {self.auto_id}, {self.start_date}, {self.end_date}'


