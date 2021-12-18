from django.core.management import BaseCommand
from ...models import *


class Command(BaseCommand):
    help = "Clear all data from audience distribution project database"

    def handle(self, *args, **options):
        if input("Are you sure? (Y/N): ") in ('y', 'Y'):
            for model in [Syllabus, Discipline, Lecturer, Group, Audience]:
                model.objects.all().delete()
