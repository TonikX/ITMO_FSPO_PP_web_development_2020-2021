from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_matushin_l2 import settings

# сделать ограничения целостности, str_def + choices modules django


class Owner(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    pass_num = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.birth_date)


class License(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()

    def __str__(self):
        return '%s %s %s %s' % (self.owner, self.number, self.type, self.issue_date)


class Auto(models.Model):
    owner = models.ManyToManyField(Owner, through='AutoOwner')
    number = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s %s %s' % (self.number, self.brand, self.model, self.color)


class AutoOwner(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now())  # autofill
    end_date = models.DateField()

    db_constraints = {
        'start_date_rule': 'check (price > 0)',
    }

    def __str__(self):
        return '%s %s %s %s' % (self.owner, self.auto, self.start_date, self.end_date)

# Create your models here.

# Реализовать вывод всех владельцев функционально.
# Добавить данные минимум от трех владельцах.
# Должны быть реализованы контроллер (views) и шаблоны (templates).
