from django.contrib.auth.models import AbstractUser
from django.db import models

from django_project_Podolskiy import settings
#   from django.contrib.auth import get_user_model


#   from project_first_app.managers import CustomUserManager


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    state_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(null=True, max_length=30)

    def __str__(self):
        return "{}".format(self.state_num)


class Owner(AbstractUser):
    #   id = models.IntegerField(primary_key=True)
    #   password = models.CharField(max_length=200, default='pbkdf2_sha256$216000$adT8u91SvCpo$kV3TG+/SyvnxVEU1TON07JQXOyksbI5Lpk+llz3eKM8=')
    #   username = None
    #   email = None
    #   is_superuser = models.BooleanField(default=True)
    #   is_staff = models.BooleanField(default=True)
    birthdate = models.DateField(null=True)
    pass_num = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=40, null=True)
    cars = models.ManyToManyField(Car, through='Ownership')

    # USERNAME_FIELD = 'id'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return str(self.username)


class Ownership(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


class License(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()

    def __str__(self):
        return str(self.num)
