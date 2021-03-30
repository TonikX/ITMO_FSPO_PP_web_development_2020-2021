from django.db import models
from django.contrib.auth.models import AbstractUser

from django_project_dusheba import settings


class Car(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


def __str__(self):
    return "{} {}".format(self.gos_number, self.mark, self.model, self.color)


class CarOwner(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(blank=True, null=True)
    passport_number = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=15, blank=True, null=True)
    # обязательные поля при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name']


def __str__(self):
    return "{} {}".format(self.first_name, self.last_name)


class Own(models.Model):
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField(blank=True, null=True)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


def __str__(self):
    return "{} {}".format(self.date_start, self.date_finish, self.id_carOwner, self.id_car)


class Doc(models.Model):
    id_carOwner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doc_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField(blank=True, null=True)


def __str__(self):
    return "{} {}".format(self.id_carOwner, self.doc_num, self.type, self.date_issue)


