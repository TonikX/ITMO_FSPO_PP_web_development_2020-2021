from django.contrib import admin

from .models import Owner, Drivers_license, Car, Possession
admin.site.register(Owner)
admin.site.register(Drivers_license)
admin.site.register(Car)
admin.site.register(Possession)