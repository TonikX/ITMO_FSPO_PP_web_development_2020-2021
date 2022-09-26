from django.core.management import BaseCommand, call_command
from netifaces import ifaddresses, interfaces, AF_INET


class Command(BaseCommand):
    help = 'Run server in local network'

    def handle(self, *args, **options):

        for ind, ifaceName in enumerate(interfaces()):
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
            print('%s. %s: %s' % (ind + 1, ifaceName, ', '.join(addresses)))

        number = input("\nChoose network interface: ")
        ifaddr = ifaddresses(interfaces()[int(number) - 1])

        print()

        call_command('runserver', '--noreload', f'{ifaddr[2][0]["addr"]}:8000')
