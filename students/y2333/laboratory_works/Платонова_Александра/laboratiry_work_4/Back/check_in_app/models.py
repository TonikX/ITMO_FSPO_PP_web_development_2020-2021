from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.core.validators import MinValueValidator


class Organizatoin(models.Model):
    name = models.CharField(max_length=100)
    legal_address = models.TextField()
    type = models.CharField(max_length=50)
    TIN = models.CharField(max_length=25)


class Address(models.Model):
    city_district = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)


class Hostel(models.Model):
    name = models.CharField(max_length=100, default="name of the hostel")
    house_num = models.IntegerField(validators=[MinValueValidator(0)])
    building = models.IntegerField(validators=[MinValueValidator(0)])
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organizatoin, on_delete=models.CASCADE)


class Room(models.Model):
    floor = models.IntegerField(validators=[MinValueValidator(0)])
    beds = models.IntegerField(validators=[MinValueValidator(0)])
    area = models.FloatField(validators=[MinValueValidator(0)])
    busy_beds = models.IntegerField(validators=[MinValueValidator(0)])
    hostel_id = models.ForeignKey(Hostel, on_delete=models.CASCADE)


class Resident(AbstractUser):
    registration_num = models.IntegerField(default=100, blank=True, null=True, validators=[MinValueValidator(0)])
    full_name = models.CharField(max_length=100, default="full_name")
    passport = models.CharField(max_length=20, blank=True, default="passport")
    children = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    educational_institution =models.CharField(max_length=100, blank=True, null=True, default="nothing")
    organization_id = models.ForeignKey(Organizatoin, on_delete=models.CASCADE, blank=True, null=True, default=1)

    REQUIRED_FIELDS = ['registration_num', 'children']


class Check_in_out(models.Model):
    doc_num = models.IntegerField(validators=[MinValueValidator(0)])
    date_of_issue = models.DateField(default=date.today, blank=True)
    comment = models.TextField(blank=True)
    check_out_reason = models.TextField(blank=True)
    date_of_checkout = models.DateField()
    doc_name = models.CharField(max_length=100)
    date_of_start = models.DateField(default=date.today)
    resident_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


class Payment(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=50, choices=[("p", "paid"), ("np", "not paid"), ("pp", "partially paid")])
    date_pay = models.DateField(default=date.today)
    check_in_out_id = models.ForeignKey(Check_in_out, on_delete=models.CASCADE, default=1)