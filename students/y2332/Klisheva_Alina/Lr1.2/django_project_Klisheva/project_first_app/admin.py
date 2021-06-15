from django.contrib import admin
from .models import Car, Car_owner, Ownership, Drivers_license
admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Ownership)
admin.site.register(Drivers_license)

