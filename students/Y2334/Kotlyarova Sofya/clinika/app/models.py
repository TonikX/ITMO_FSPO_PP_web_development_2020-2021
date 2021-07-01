from django.db import models
import datetime


class Service(models.Model):
    name = models.CharField(max_length=64)


class Doctor(models.Model):
    name = models.CharField(max_length=64, default='Анна Генадьевна')
    phone = models.CharField(max_length=64, default='+79112811575')
    speciality = models.CharField(max_length=64, default='стоматолог')


class DoctorService(models.Model):
    price = models.IntegerField(default=0)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=64, default='Анна Генадьевна')
    phone = models.CharField(max_length=64, default='+79112811575')
    document_number = models.CharField(max_length=6, default='000001', unique=True)


class Ticket(models.Model):
    client = models.ForeignKey(Client, default=None, blank=True, null=True, on_delete=models.SET_NULL)
    doctor_service = models.ForeignKey(DoctorService, on_delete=models.CASCADE)
    when = models.DateField(default=datetime.date.today, blank=True)
