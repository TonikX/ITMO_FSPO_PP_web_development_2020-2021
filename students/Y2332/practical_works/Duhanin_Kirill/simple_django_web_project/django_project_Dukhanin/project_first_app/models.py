from django.db.models import *
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    birthdate = DateField(null=True)
    passport_number = CharField(max_length=10)
    address = TextField()
    nationality = TextField()
    password = TextField()
    username = TextField(unique=True)
    is_superuser = BooleanField(default=False)
    # last_name = CharField(max_length=50)

    # email = TextField()


class DriverLicense(Model):
    owner_id = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    number = CharField(max_length=20)
    date = DateTimeField()


class Car(Model):
    state_number = CharField(max_length=15)
    brand = CharField(max_length=20)
    model = CharField(max_length=20)
    color = CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.state_number}, {self.model}'


class Ownership(Model):
    owner_id = ForeignKey(Owner, null=True, on_delete=CASCADE)
    car_id = ForeignKey(Car, null=True, on_delete=CASCADE)
    start_date = DateTimeField()
    end_date = DateTimeField(null=True)
