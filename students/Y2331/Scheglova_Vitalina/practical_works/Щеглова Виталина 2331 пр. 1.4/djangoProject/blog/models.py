from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=500, default="NULL")
    passport_number = models.CharField(max_length=10, default="NULL")
    nationality = models.CharField(max_length=15, default="NULL")

    def __str__(self):
        return "{}{}{}{}{}{}".format(self.last_name, self.name, self.birth_date, self.address, self.passport_number,
                                     self.nationality)


class Car(models.Model):
    State_number = models.CharField(max_length=15)
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=30)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    # На вход идут строки, на выходе они получают форматирование и специальный вывод
    def __str__(self):
        return "{}".format(self.owner)


class Drivers_license(models.Model):
    owner_drivers_license = models.ForeignKey(Owner,
                                              on_delete=models.CASCADE)  # создание ключа овнер в таблице воддительское удостоверение, если удалится удостоверение, то удалится и овнер
    number_of_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()


class Possession(models.Model):
    owner_possession = models.ForeignKey(Owner,
                                         on_delete=models.CASCADE)  # создание ключа овнер в таблице владелец, если удалится владелец, то удалится и овнер
    the_date_of_the_beginning = models.DateField()
    expiration_date = models.DateField()
    car_possession = models.ForeignKey(Car,
                                       on_delete=models.CASCADE)  # создание ключа машина в таблице владелец, если удалится владелец, то удалится и машина

    # Создание новой модели с именем "ExampleModel"


class ExampleModel(models.Model):
    # поля модели
    title = models.CharField(max_length=200)
    description = models.TextField()

    # метод ожидает только экземпляр и должен возвращать строку,берет title
    def __str__(self):
        return self.title


class Publisher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # На вход идут строки, на выходе они получают форматирование и специальный вывод. Модель также может иметь методы. Минимально в каждой модели вы должны определить стандартный метод класса для Python __str __ (), чтобы вернуть удобочитаемую строку для каждого объекта.
    def __str__(self):  # Этот метод возвращает строковое представление объекта.
        return "{} {}".format(self.first_name, self.last_name)
