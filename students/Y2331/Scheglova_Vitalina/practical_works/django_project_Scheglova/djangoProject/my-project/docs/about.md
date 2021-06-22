# Создание модели данных Django ORM
```python
from django.db import models
from django.db.models import CharField


class Plane_type(models.Model): # Модель типа самолета
    model_name = models.CharField(max_length=20) # Имя модели
    manufacturer = models.CharField(max_length=20) # Изготовитель
    capacity = models.IntegerField() # Вместимость

class Plane(models.Model): # Модель самолета
    last_date_of_check = models.DateField() # Дата последней проверки
    made_year = models.DateField() # Дата изготовления
    plane_type = models.CharField(max_length=20) # Тип самолета
    plane_name = models.ForeignKey(Plane_type, on_delete=models.CASCADE) # Имя модели


class Client(models.Model): # Модель клиента
    FIO_client = models.CharField(max_length=50) # ФИО клиента
    passport_number = models.IntegerField() # Паспортный номер
    date_of_passport_start = models.DateField() # Дата начала паспорта
    registration_number = models.IntegerField() # Регистрационный номер
    who_give_the_passport = models.CharField(max_length=100) # Кто выдал паспорт


class Ticket_office(models.Model): # Модель билетного офиса
    ticket_office_adress = models.CharField(max_length=60) # Адрес билетного офиса

class Cashier(models.Model): # Модель кассира
    cashier_FIO = models.CharField(max_length=60) # ФИО кассира
    ticket_office_name = models.ForeignKey(Ticket_office, on_delete=models.CASCADE) # Адрес билетного офиса

class Ticket(models.Model):  # Модель билета
    type_ticket = models.CharField(max_length=20) # Тип билета
    cost = models.IntegerField() # Цена
    ticket_status = models.CharField(max_length=20) # Статус билета
    ticket_class = models.CharField(max_length=20) # Класс билета
    ticket_number = models.IntegerField() # Номер билета
    cashier_name = models.ForeignKey(Cashier, on_delete=models.CASCADE) # ФИО кассира

class Order(models.Model): # Модель заказа
    order_date = models.DateField() # Дата заказа
    order_status = models.CharField(max_length=20) # Статус заказа
    ticket_name = models.ForeignKey(Ticket, on_delete=models.CASCADE) # Номер билета
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE) # ФИО клиента

class Flight(models.Model): # Модель полета
    time_flight_start = models.DateTimeField() # Время начала полета
    time_flight_finish = models.DateTimeField() # Время конца полета
    date_flight_start = models.DateField() # Дата начала полета
    date_flight_finish = models.DateField() # Дата конца полета
    name_of_flight = models.CharField(max_length=20) # Название полета
    airport_start = models.CharField(max_length=40) # Аэропорт начальный
    airport_finish = models.CharField(max_length=40) # Аэропорт конечный
    type_of_flight = models.CharField(max_length=20) # Тип полета
    board_name = models.ForeignKey(Plane, on_delete=models.CASCADE) # Название 
    ticket_name = models.ForeignKey(Ticket, on_delete=models.CASCADE) # Номер билета


class Transit_boarding(models.Model): # Модель транзитной посадки
    transit_airport = models.CharField(max_length=20) # Название транзитного аэропорта
    date_flight_start = models.DateField() # Дата полета начало
    date_flight_finish = models.DateField() # Дата полета конец
    time_flight_start = models.DateTimeField() # Время полета начало
    time_flight_finish = models.DateTimeField() # Время полета конец
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE) # Номер полета

class Staff(models.Model): # Модель рабочих
    employee_position = models.CharField(max_length=50) # Должность
    employee_FIO = models.CharField(max_length=60) # ФИО
    people = models.ManyToManyField(Flight, through='Crew') # Люди

class Crew(models.Model): # Модель экипажа
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) # Рабочие
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE) # Название полета

```
