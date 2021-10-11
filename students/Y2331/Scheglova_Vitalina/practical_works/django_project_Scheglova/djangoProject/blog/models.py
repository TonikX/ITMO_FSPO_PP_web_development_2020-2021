from django.db import models
from django.db.models import CharField


class Plane_type(models.Model):
    model_name = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    capacity = models.IntegerField()

class Plane(models.Model):
    last_date_of_check = models.DateField()
    made_year = models.DateField()
    plane_type = models.CharField(max_length=20)
    plane_name = models.ForeignKey(Plane_type, on_delete=models.CASCADE)


class Client(models.Model):
    FIO_client = models.CharField(max_length=50)
    passport_number = models.IntegerField()
    date_of_passport_start = models.DateField()
    registration_number = models.IntegerField()
    who_give_the_passport = models.CharField(max_length=100)


class Ticket_office(models.Model):
    ticket_office_adress = models.CharField(max_length=60)

class Cashier(models.Model):
    cashier_FIO = models.CharField(max_length=60)
    ticket_office_name = models.ForeignKey(Ticket_office, on_delete=models.CASCADE)

class Ticket(models.Model):
    type_ticket = models.CharField(max_length=20)
    cost = models.IntegerField()
    ticket_status = models.CharField(max_length=20)
    ticket_class = models.CharField(max_length=20)
    ticket_number = models.IntegerField()
    cashier_name = models.ForeignKey(Cashier, on_delete=models.CASCADE)

class Order(models.Model):
    order_date = models.DateField()
    order_status = models.CharField(max_length=20)
    ticket_name = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)

class Flight(models.Model):
    time_flight_start = models.DateTimeField()
    time_flight_finish = models.DateTimeField()
    date_flight_start = models.DateField()
    date_flight_finish = models.DateField()
    name_of_flight = models.CharField(max_length=20)
    airport_start = models.CharField(max_length=40)
    airport_finish = models.CharField(max_length=40)
    type_of_flight = models.CharField(max_length=20)
    board_name = models.ForeignKey(Plane, on_delete=models.CASCADE)
    ticket_name = models.ForeignKey(Ticket, on_delete=models.CASCADE)


class Transit_boarding(models.Model):
    transit_airport = models.CharField(max_length=20)
    date_flight_start = models.DateField()
    date_flight_finish = models.DateField()
    time_flight_start = models.DateTimeField()
    time_flight_finish = models.DateTimeField()
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)

class Staff(models.Model):
    employee_position = models.CharField(max_length=50)
    employee_FIO = models.CharField(max_length=60)
    people = models.ManyToManyField(Flight, through='Crew')

class Crew(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

