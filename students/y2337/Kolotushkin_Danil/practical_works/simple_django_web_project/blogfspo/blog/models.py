from django.db import models

# Create your models here.

class car(models.Model):
    gov_number = models.CharField(max_length = 15)
    brand = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    color = models.CharField(max_length = 30)
class owner(models.Model):
    last_name = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    borndate = models.DateTimeField()


class card(models.Model):
    owner_ID = models.ForeignKey(owner, on_delete = models.CASCADE)
    card_number = models.CharField(max_length = 10)
    type = models.CharField(max_length = 10)
    getdate = models.DateTimeField()

class owning(models.Model):
    owner_ID = models.ForeignKey(owner, on_delete = models.CASCADE)
    car_ID = models.ForeignKey(car, on_delete = models.CASCADE)
    begin = models.DateTimeField()
    end = models.DateTimeField() 

   
