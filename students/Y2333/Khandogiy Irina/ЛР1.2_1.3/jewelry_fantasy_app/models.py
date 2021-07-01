import datetime

from django.core.validators import *
from django.db import models


# Продукция
# Продавец
# Продажа
# Поставщик
# Поставка


class Production(models.Model):
    TYPE = [
        ('1', 'Rings'),
        ('2', 'Earrings'),
        ('3', 'Chains'),
        ('4', 'Bracelets'),
        ('5', 'Pendants'),
        ('6', 'Necklace'),
        ('7', 'Charms'),
        ('8', 'Another'),
    ]
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=10, choices=TYPE, default='8')
    num = models.PositiveIntegerField(default=0)
    photo = models.ImageField(null=True, blank=True, )

    def __str__(self):

        return self.name


class Seller(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patr = models.CharField(max_length=30)
    birth = models.DateField()
    salary = models.PositiveIntegerField(default=0)
    exp = models.PositiveSmallIntegerField(default=0)
    address = models.CharField(max_length=45)
    education = models.CharField(max_length=45, blank=True)

    def save(self, *args, **kwargs):
        bd = self.birth
        td = datetime.date.today()
        if bd.year - ((td.month, td.day) < (bd.month, bd.day)) >= datetime.date.today().year - 18:
            raise ValidationError("The employee must be over 18 years of age!")
        super(Seller, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return '%s %s %s' % (self.surname, self.name, self.patr)

    def __str__(self):
        return self.full_name


class Sale(models.Model):
    product = models.ForeignKey(Production, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())
    price = models.PositiveIntegerField()
    num = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        if self.date > datetime.date.today():
            raise ValidationError("The date cannot be in the future!")
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return self.date


class Factory(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Supply(models.Model):
    product = models.ForeignKey(Production, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    post_date = models.DateField()
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.post_date
