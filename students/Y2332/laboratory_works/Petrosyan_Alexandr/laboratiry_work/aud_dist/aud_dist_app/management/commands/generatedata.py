import random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from aud_dist_app.models import *
from ..lists import DISCIPLINES, AUDIENCE_TYPES


class Provider(faker.providers.BaseProvider):
    def discipline(self):
        return self.random_element(DISCIPLINES)

    def audience_type(self):
        return self.random_element(AUDIENCE_TYPES)


def generate_disciplines(fake):
    for _ in range(random.randint(10, len(DISCIPLINES))):
        Discipline.objects.create(
            name=fake.unique.discipline()
        )


def generate_lecturers(fake, first_discipline, last_discipline):
    for _ in range(random.randint(10, 20)):
        lecturer = Lecturer.objects.create(
            first_name=fake.first_name_male(),
            surname=fake.last_name_male(),
            patronymic=fake.middle_name_male(),
        )

        for _ in range(random.randint(1, 3)):
            rand_discipline = random.randint(first_discipline, last_discipline)
            discipline = Discipline.objects.get(pk=rand_discipline)
            lecturer.disciplines.add(discipline)

        lecturer.save()


def generate_groups(fake, first_discipline, last_discipline, discipline_quantity):
    for _ in range(random.randint(5, 10)):
        group = Group.objects.create(
            number=fake.plate_letter() + fake.plate_number_extra(),
            students_quantity=random.randint(18, 25)
        )

        for _ in range(random.randint(10, discipline_quantity)):
            rand_discipline = random.randint(first_discipline, last_discipline)
            discipline = Discipline.objects.get(pk=rand_discipline)
            group.disciplines.add(discipline)

        group.save()


def generate_audiences(fake):
    for _ in range(random.randint(15, 25)):
        Audience.objects.create(
            number=random.randint(100, 999),
            aud_type=fake.audience_type()
        )


class Command(BaseCommand):
    help = "Generate data for audience distribution project"

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        fake.add_provider(Provider)

        try:
            discipline_quantity = Discipline.objects.count()

            if discipline_quantity < 10:
                if input("Not enough disciplines. Generate them? (Y/N): ") in ('y', 'Y'):
                    generate_disciplines(fake)
                else:
                    raise Exception("Error: Not enough disciplines (should be more than 10)")

            discipline_quantity = Discipline.objects.count()

            first_discipline = Discipline.objects.first().pk
            last_discipline = Discipline.objects.last().pk

            generate_lecturers(fake, first_discipline, last_discipline)
            generate_groups(fake, first_discipline, last_discipline, discipline_quantity)
            generate_audiences(fake)

        except Exception as e:
            print(str(e))