from django.contrib import admin

from .models import Owner, Ownering, Car, Driver_license

admin.site.register(Owner)
admin.site.register(Ownering)
admin.site.register(Car)
admin.site.register(Driver_license)

# Register your models here.
