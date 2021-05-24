import random

from django.core.management.base import BaseCommand
from faker import Faker
from aud_dist_app.models import *


def generate_disciplines():
    # TODO
    ...


def generate_lecturers(faker, first_discipline, last_discipline):
    for _ in range(random.randint(10, 20)):
        lecturer = Lecturer.objects.create(
            first_name=faker.first_name_male(),
            surname=faker.last_name_male(),
            patronymic=faker.middle_name_male(),
        )

        for _ in range(random.randint(1, 3)):
            rand_discipline = random.randint(first_discipline, last_discipline)
            discipline = Discipline.objects.get(pk=rand_discipline)
            lecturer.disciplines.add(discipline)

        lecturer.save()


def generate_groups(faker, first_discipline, last_discipline, discipline_quantity):
    for _ in range(random.randint(3, 5)):
        group = Group.objects.create(
            number=faker.plate_letter() + faker.plate_number_extra()
        )
        group.students_quantity = random.randint(18, 25)

        for _ in range(random.randint(10, discipline_quantity)):
            rand_discipline = random.randint(first_discipline, last_discipline)
            discipline = Discipline.objects.get(pk=rand_discipline)
            group.disciplines.add(discipline)

        group.save()


class Command(BaseCommand):
    help = "Generate data for audience distribution project"

    def handle(self, *args, **options):
        faker = Faker('ru_RU')

        try:
            discipline_quantity = Discipline.objects.count()

            if discipline_quantity < 10:
                if input("Not enough disciplines. Generate them? (Y/N): ") in ('y', 'Y'):
                    generate_disciplines()
                    discipline_quantity = Discipline.objects.count()
                else:
                    raise Exception("Error: Not enough disciplines (should be more than 10)")

            first_discipline = Discipline.objects.first().pk
            last_discipline = Discipline.objects.last().pk

            generate_lecturers(faker, first_discipline, last_discipline)
            generate_groups(faker, first_discipline, last_discipline, discipline_quantity)

        except Exception as e:
            print(str(e))
