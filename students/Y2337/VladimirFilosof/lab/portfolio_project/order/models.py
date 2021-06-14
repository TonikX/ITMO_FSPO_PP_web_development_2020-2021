from django.contrib.auth.models import AbstractUser
from django.db import models

from portfolio_project import settings


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField()
    preview = models.ImageField(upload_to='img/service/', max_length=255)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)


class User(AbstractUser):
    orders = models.ManyToManyField(Service, through=Order)
