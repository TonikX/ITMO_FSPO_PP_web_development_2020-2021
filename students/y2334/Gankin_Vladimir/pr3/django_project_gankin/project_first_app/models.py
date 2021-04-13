from django.db import models


# Create your models here.
class Auto(models.Model):
    number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return "{} {}".format(self.number, self.brand, self.model, self.color)


class AutoOwner(models.Model):
    ownership = models.ManyToManyField(Auto, through='Owning')
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Owning(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    auto_owner = models.ForeignKey(AutoOwner, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True)


class DriverLicense(models.Model):
    auto_owner = models.ForeignKey(AutoOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date = models.DateTimeField(null=False)
