import random

import faker
from django.core.management.base import BaseCommand
from faker import Faker
from aud_dist_app.models import *


class Command(BaseCommand):
    help = "Command info"

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        first_discipline = Discipline.objects.first().pk
        last_discipline = Discipline.objects.last().pk

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
