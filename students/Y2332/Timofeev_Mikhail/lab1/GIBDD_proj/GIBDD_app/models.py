from django.contrib.auth.models import AbstractUser
from django.db.models import *


class User(AbstractUser):
    tel = CharField(max_length=10)

    REQUIRED_FIELDS = ['first_name', 'last_name']


class Body(Model):
    body_type = TextField(unique=False)
    body_model = TextField(unique=True)

    def __str__(self) -> str:
        return f'Кузов тип: {self.body_type} модель: {self.body_model}'


class Engine(Model):
    engine_type = TextField(unique=True)
    power = IntegerField()
    volume = IntegerField()

    def __str__(self) -> str:
        return f'Двигатель тип: {self.engine_type} мощность: {self.power} объём {self.volume}'


class CarModel(Model):
    model = TextField(unique=True)
    brand = CharField(max_length=15)
    producer = CharField(max_length=60)

    engine_id = ForeignKey('Engine', on_delete=CASCADE)
    body_id = ForeignKey('Body', on_delete=CASCADE)

    def __str__(self) -> str:
        return f'Модель {self.model} марка: {self.brand}, производитель: {self.producer}'


class LegalOwner(Model):
    owner_inn = CharField(max_length=10, unique=True)
    owner_name = CharField(max_length=60)
    chief = CharField(max_length=60)
    phone = CharField(max_length=11)

    def __str__(self) -> str:
        return f'Юридический владелец {self.owner_name} ИНН: {self.owner_inn}, руководитель: {self.chief}, телефон: {self.phone}'


class PhysicalOwner(Model):
    owner_id = IntegerField(unique=True)
    owner_fullname = CharField(max_length=60)
    phone = CharField(max_length=11)
    address = TextField()

    def __set_name__(self) -> str:
        return f'Физический владелец {self.owner_fullname} ИНН: {self.owner_id}, телефон: {self.phone}, адрес: {self.address}'


class Car(Model):
    car_number = CharField(max_length=10, unique=True)
    helm = BooleanField()
    drive = BooleanField()
    year = IntegerField()
    owner_type = BooleanField()
    district = TextField()
    year_tax = FloatField()
    comment = TextField(blank=True)
    color = TextField()

    model = ForeignKey('CarModel', on_delete=CASCADE)
    owner_inn = ForeignKey('LegalOwner', null=True, on_delete=CASCADE)
    owner_id = ForeignKey('PhysicalOwner', null=True, on_delete=CASCADE)

    def __str__(self) -> str:
        owner = self.owner_inn if self.owner_id is None else self.owner_id
        return f'Автомобиль {self.car_number} владелец: {owner}, модель: {self.model}'


class DriveAwayInfo(Model):
    driving_away = BooleanField()
    date_away = DateField(null=True)
    date_return = DateField(null=True)

    car_number = ForeignKey('Car', on_delete=CASCADE)

    def __str__(self) -> str:
        return f'Информация об угоне номер: {self.id}, автомобиль: {self.car_number}'


class Inspector(Model):
    sign_number = CharField(max_length=7, unique=True)
    fullname = TextField()
    post = TextField()

    def __str__(self) -> str:
        return f'Инспектор {self.fullname} номер значка: {self.sign_number}, должность: {self.post}'


class WatchInfo(Model):
    watch_date = DateField()
    sign_cost = FloatField()
    watch_cost = FloatField()
    mileage = FloatField()
    okay = BooleanField()
    reasons = TextField(blank=True)

    car_number = ForeignKey('Car', on_delete=CASCADE)
    inspector = ForeignKey('Inspector', on_delete=CASCADE)

    def __str__(self) -> str:
        return f'Осмотр номер {self.id} автомобиль: {self.car_number} инспектор: {self.inspector}'
