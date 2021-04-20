from django.contrib import admin

from .models import Owner, Car, Ownering, Driver_license
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownering)
admin.site.register(Driver_license)