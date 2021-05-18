from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.utils.translation import *
from django.contrib.auth.models import User

User = get_user_model()


class Cafe(models.Model):
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    director_surname = models.CharField(max_length=25)
    computer_number = models.IntegerField()

    def __str__(self):
        return self.title


class Computer(models.Model):
    title = models.CharField(max_length=30)
    registration_number = models.IntegerField()
    year_of_purchase = models.DateField()
    service_life = models.IntegerField()
    hour_online = models.DecimalField(max_digits=9, decimal_places=2)
    hour_game = models.DecimalField(max_digits=9, decimal_places=2)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, null=True)
    online_use = models.IntegerField(default=0)
    game_use = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    order_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.id)

    def __str__(self, user):
        return str(user.id)
