from django.contrib import admin

from .models import Car, Car_owner, Drivers_license, Ownership


admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Drivers_license)
admin.site.register(Ownership)
