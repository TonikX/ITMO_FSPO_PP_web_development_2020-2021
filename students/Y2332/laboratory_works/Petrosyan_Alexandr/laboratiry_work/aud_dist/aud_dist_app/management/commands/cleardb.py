from django.core.management import BaseCommand
from aud_dist_app.models import *


class Command(BaseCommand):
    help = "Clear all data from audience distribution project database"

    def handle(self, *args, **options):
        if input("Are you sure? (Y/N): ") in ('y', 'Y'):
            Discipline.objects.all().delete()
            Lecturer.objects.all().delete()
            Group.objects.all().delete()
            Audience.objects.all().delete()
