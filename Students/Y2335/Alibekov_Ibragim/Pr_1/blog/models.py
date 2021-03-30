from django.db import models


class Owner(models.Model):
    last_name = models.CharField('Фамилия', max_length=30)
    first_name = models.CharField('Имя', max_length=30)
    date_of_birth = models.DateTimeField(null=True)


class Car(models.Model):
    DoesNotExist = None
    country_number = models.CharField(max_length=15)
    brand = models.CharField('Марка', max_length=20)
    model = models.CharField('Модель', max_length=20)
    color = models.CharField('Цвет', max_length=30, null=True)


class Possession(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE,  null=True)
    date_of_start = models.DateTimeField()
    expiration_date = models.DateTimeField(null=True)
    models.ManyToManyField(Owner, through='possession')


class License(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number_of_license = models.CharField('Номер лицензии', max_length=10)
    type = models.CharField('Тип', max_length=10)
    date_of_issue = models.DateTimeField()