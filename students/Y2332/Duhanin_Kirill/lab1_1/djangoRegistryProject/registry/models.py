from typing import Type

from django.contrib.auth.decorators import user_passes_test
from django.db.models import *
import hashlib

from generator import generate_views, generate_to_str


class CardModel(Model):
    id = CharField(primary_key=True, max_length=256)
    description = TextField()
    root = CharField(max_length=30)
    name = CharField(max_length=30)

    @classmethod
    def create(cls, id, description, root, name):
        return cls(id=id, description=description, root=root, name=name)


def generate_card(model: Type[Model]):
    fields = ' '.join(map(lambda t: t[0] + str(type(t[1])), model.__dict__))
    model_hash = hashlib.sha256((model.__name__ ).encode()).hexdigest()
    CardModel.create(model_hash, model.__doc__, model.__name__.lower(), model.__name__).save()
    return model


@generate_views(root_path='/building')
@generate_to_str.from_pattern('Здание @name по адресу @address ')
@generate_card
class Building(Model):
    """
    Building model...
    @:param 34234
    """
    name = CharField(max_length=40)
    land = IntegerField()
    address = TextField(null=False)
    year = IntegerField()
    material = CharField(max_length=20)


@generate_views(root_path='/department')
@generate_to_str.from_pattern('@type @name (@phone)')
@generate_card
class Department(Model):
    name = CharField(max_length=40)
    boss = CharField(max_length=40)
    phone = CharField(max_length=10)
    office_dean = CharField(max_length=30)
    building = ForeignKey(Building.model, on_delete=CASCADE)
    start_date = DateField()
    type = CharField(max_length=20) # todo add choises


@generate_views(root_path='/worker')
@generate_to_str.from_pattern('Работник @name (@service_number, @phone)')
@generate_card
class Worker(Model):
    service_number = IntegerField()
    address = CharField(max_length=100)
    name = CharField(max_length=100)
    phone = CharField(max_length=10)


@generate_views(root_path='/management')
@generate_to_str.from_pattern('Работник с номером @worker_service_number'
                              ' управляет подразделением с номером @department_id')
@generate_card
class Management(Model):
    start_date = DateField()
    end_date = DateField(null=True)

    worker = ForeignKey(Worker.model, on_delete=CASCADE)
    department = ForeignKey(Department.model, on_delete=CASCADE)


@generate_views(root_path='/hall')
@generate_to_str.from_pattern('Аудитория @code @target')
@generate_card
class Hall(Model):
    code = IntegerField()
    square = IntegerField(null=True)
    window = IntegerField(null=True)
    heating = IntegerField(null=True)
    target = CharField(max_length=15) # todo choises

    department = ForeignKey(Department.model, on_delete=CASCADE)


@generate_views(root_path='/responsibility')
@generate_to_str.from_pattern('Работник с номером @worker_service_number '
                              'несет ответственность за аудиторию с номером @hall_id ')
@generate_card
class Responsibility(Model):
    start_date = DateField()
    end_date = DateField(null=True)

    hall = ForeignKey(Hall.model, on_delete=CASCADE)
    worker = ForeignKey(Worker.model, on_delete=CASCADE)


@generate_views(root_path='/property')
@generate_to_str()
@generate_card
class Property(Model):
    standard_code = IntegerField(primary_key=True, auto_created=True)
    name = CharField(max_length=20)


@generate_views(root_path='/unit')
@generate_to_str.from_pattern('Единица имущества @name с номером @id')
@generate_card
class Unit(Model):
    id = IntegerField(primary_key=True, auto_created=True)
    name = CharField(max_length=30)
    date_start = DateField()
    cost = IntegerField()
    period = IntegerField()
    standard_code = ForeignKey(Property.model, on_delete=CASCADE)


@generate_views(root_path='/consist')
@generate_to_str.from_pattern('Аудитория с номером @hall_id содержит единицу имущества с номером @unit_id')
@generate_card
class Consist(Model):
    start_date = DateField()
    end_date = DateField(null=False)

    unit = ForeignKey(Unit.model, on_delete=CASCADE)
    hall = ForeignKey(Hall.model, on_delete=CASCADE)


@generate_views(root_path='/revaluation')
@generate_to_str.from_pattern('Переоценка от @date изменила стоимость '
                              'единицы имущества с номером @unit_id c @cost_before на @cost_after руб')
@generate_card
class Revaluation(Model):
    unit = ForeignKey(Unit.model, on_delete=CASCADE)
    date = DateField()
    cost_after = IntegerField()
    cost_before = IntegerField()


