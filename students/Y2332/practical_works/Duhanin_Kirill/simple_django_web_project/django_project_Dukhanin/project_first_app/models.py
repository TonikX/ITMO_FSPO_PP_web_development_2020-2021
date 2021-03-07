from django.db.models import *


class Owner(Model):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    birthdate = DateTimeField(null=True)


class DriverLicense(Model):
    owner_id = ForeignKey(Owner, on_delete=CASCADE)
    number = CharField(max_length=20)
    date = DateTimeField()


class Car(Model):
    state_number = CharField(max_length=15)
    brand = CharField(max_length=20)
    model = CharField(max_length=20)
    color = CharField(max_length=30, null=True)


class Ownership(Model):
    owner_id = ForeignKey(Owner, null=True, on_delete=CASCADE)
    car_id = ForeignKey(Car, null=True, on_delete=CASCADE)
    start_date = DateTimeField()
    end_date = DateTimeField(null=True)


class ExampleModel(Model):
    title = CharField(max_length=200)
    description = TextField()

    def __str__(self):
        return self.title


class Publisher(Model):
    first_name = CharField(max_length=30)
    second_name = CharField(max_length=30)
    birthdate = DateField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Book(Model):
    name = CharField(max_length=100)
    desc = CharField(max_length=200)
    publisher = ForeignKey(Publisher, on_delete=CASCADE)

    def __str__(self):
        return f"{self.name} {self.publisher}"
