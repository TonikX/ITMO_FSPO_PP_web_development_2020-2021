from django.db import models
from django.contrib.auth.models import AbstractUser


class Renter(models.Model):
    idRenter = models.IntegerField(primary_key=True)
    passport = models.CharField("Person's passport", max_length=12)
    privilege = models.FloatField("Person's privilege")
    firstName = models.CharField("First name", max_length=20)
    surname = models.CharField("Surname", max_length=20)
    patronymic = models.CharField("Patronymic", max_length=20)

    class Meta:
        ordering = ['idRenter']


class Adress(models.Model):
    idAdress = models.IntegerField(primary_key=True)
    district = models.CharField("District", max_length=20)
    street = models.CharField("Street", max_length=20)

    class Meta:
        ordering = ['idAdress']


class House(models.Model):
    idAdress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    idBuilding = models.IntegerField(primary_key=True)
    buildingNumb = models.IntegerField("Number of building")
    building = models.IntegerField("Corps")

    class Meta:
        ordering = ['idBuilding']


class Inspector(AbstractUser):
    servNumb = models.IntegerField("Service number", primary_key=True)
    phone = models.CharField("Phone number", max_length=12)
    first_name = models.CharField("First name", max_length=20)
    last_name = models.CharField("Surname", max_length=20)
    patronymic = models.CharField("Patronymic", max_length=20)
    is_staff = models.BooleanField(default=True)

    class Meta:
        ordering = ['servNumb']


class Flat(models.Model):
    idFlat = models.IntegerField(primary_key=True)
    flat = models.IntegerField("Flat")
    flatType = models.CharField("Flat type", max_length=30)
    eStove1 = 'Is present'
    eStove2 = 'Isn\'t present'
    eStoveChoices = (
        (eStove1, "Is present"),
        (eStove2, "Isn't present")
    )
    eStove = models.CharField("Availability of electric stove", max_length=13, choices=eStoveChoices, default=eStove2)
    peopleCount = models.IntegerField("People count")
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idFlat']


class Bypass(models.Model):
    bypassNumb = models.IntegerField("Bypass number", primary_key=True)
    dateOfBypass = models.DateField("Bypass date")
    status1 = 'completed'
    status2 = 'uncompleted'
    statusChoices = (
        (status1, 'completed'),
        (status2, 'uncompleted')
    )
    status = models.CharField("Bypass status", max_length=11, choices=statusChoices, default=status2)
    comment = models.CharField("Comment", max_length=100, blank=True)
    inspectorServNumb = models.ForeignKey(Inspector, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)

    class Meta:
        ordering = ['bypassNumb']
