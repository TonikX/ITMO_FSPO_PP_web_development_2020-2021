from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(null=True, blank=True)

class DriveLicense(models.Model):
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_num = models.CharField(max_length=10)
    tipe = models.CharField(max_length=10)
    date = models.DateTimeField()

class Car(models.Model):
    #MARK = models.TextChoices('BMW', 'Mitsubishi', 'Lada')
    state_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)#, choices= MARK.choices)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True)
    owner = models.ManyToManyField(Owner, through='Ownership')

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

