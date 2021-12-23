import random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from ..lists import DISCIPLINES, AUDIENCE_TYPES
from ...models import *


class Provider(faker.providers.BaseProvider):
    def discipline(self):
        return self.random_element(DISCIPLINES)

    def audience_type(self):
        return self.random_element(AUDIENCE_TYPES)


def generate_disciplines(fake):
    for _ in range(random.randint(1, len(DISCIPLINES))):
        rand_discipline = fake.unique.discipline()

        hours_total = random.randint(30, 150)
        part_max_hours = int(hours_total / 5)

        Discipline.objects.create(
            name=rand_discipline[0],
            code=rand_discipline[1],
            syllabus_id=Syllabus.objects.first().pk,
            cycle=rand_discipline[2],
            hours_total=hours_total,
            hours_lec=random.randint(1, part_max_hours),
            hours_pr=random.randint(1, part_max_hours),
            hours_la=random.randint(1, part_max_hours),
            hours_isw=random.randint(1, part_max_hours),
            hours_cons=random.randint(1, part_max_hours),
        )


def generate_lecturers(fake, first_discipline, last_discipline):
    for _ in range(random.randint(15, 25)):
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


def generate_groups(fake, first_discipline, last_discipline, discipline_count):
    for _ in range(random.randint(15, 25)):
        Group.objects.create(
            number=fake.plate_letter() + fake.plate_number_extra(),
            students_count=random.randint(18, 25),
            syllabus_id=Syllabus.objects.first().pk,
        )


def generate_audiences(fake):
    for _ in range(random.randint(15, 25)):
        Audience.objects.create(
            number=random.randint(100, 999),
            aud_type=fake.audience_type(),
            seats_count=random.randint(15, 50),
        )


def generate_schedule(
        first_discipline,
        last_discipline,
        first_lecturer,
        last_lecturer,
        first_audience,
        last_audience,
        first_group,
        last_group,
):
    for group in range(first_group, last_group):
        for day in range(1, random.randint(4, 7)):
            for lecture in range(1, random.randint(3, 7)):
                rand_lecturer = random.randint(first_lecturer, last_lecturer)
                rand_discipline = random.randint(first_discipline, last_discipline)
                rand_audience = random.randint(first_audience, last_audience)

                Schedule.objects.create(
                    lecturer_id=rand_lecturer,
                    discipline_id=rand_discipline,
                    group_id=group,
                    audience_id=rand_audience,
                    day_of_the_week=day,
                    lecture_begin=lecture,
                    lecture_type=random.randint(1, 5),
                    semester=random.randint(1, 8),
                    week_parity=bool(random.getrandbits(1))
                )


class Command(BaseCommand):
    help = "Generate data for audience distribution project"

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        fake.add_provider(Provider)

        try:
            generate_disciplines(fake)

            discipline_count = Discipline.objects.count()

            first_discipline = Discipline.objects.first().pk
            last_discipline = Discipline.objects.last().pk

            generate_lecturers(
                fake,
                first_discipline,
                last_discipline
            )
            generate_groups(
                fake,
                first_discipline,
                last_discipline,
                discipline_count
            )
            generate_audiences(fake)

            first_lecturer = Lecturer.objects.first().pk
            last_lecturer = Lecturer.objects.last().pk
            first_audience = Audience.objects.first().pk
            last_audience = Audience.objects.last().pk
            first_group = Group.objects.first().pk
            last_group = Group.objects.last().pk

            generate_schedule(
                first_discipline,
                last_discipline,
                first_lecturer,
                last_lecturer,
                first_audience,
                last_audience,
                first_group,
                last_group,
            )

        except Exception as e:
            print(str(e))
