from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.


class auto(models.Model):
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

class User(AbstractUser):
    # last_name = models.CharField(max_length=30)
    # first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    models.ManyToManyField(auto, through='ownership')
    passport = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

class autoOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    models.ManyToManyField(auto, through='ownership')

class ownership(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auto_id = models.ForeignKey(auto, on_delete=models.CASCADE)

class driverDocuments(models.Model):
    document_number = models.CharField(max_length=10)
    document_type = models.CharField(max_length=10)
    document_date = models.DateField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
