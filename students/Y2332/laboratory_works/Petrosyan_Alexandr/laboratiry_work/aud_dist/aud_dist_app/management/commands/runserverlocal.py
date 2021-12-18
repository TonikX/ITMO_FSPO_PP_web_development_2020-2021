from django.core.management import BaseCommand, call_command
from netifaces import ifaddresses, interfaces, AF_INET

from ..interface import INTERFACE


class Command(BaseCommand):
    help = 'Run server in local network'

    def handle(self, *args, **options):

        # Used to get current machine network interfaces
        # for ifaceName in interfaces():
        #     addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        #     print ('%s: %s' % (ifaceName, ', '.join(addresses)))

        ifaddr = ifaddresses(INTERFACE)
        call_command('runserver', f'{ifaddr[2][0]["addr"]}:8000')
