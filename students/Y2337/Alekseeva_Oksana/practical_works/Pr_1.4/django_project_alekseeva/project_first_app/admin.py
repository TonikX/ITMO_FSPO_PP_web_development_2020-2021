from django.contrib import admin
from .models import Car, Car_owner, Ownership, Driving_license
# Register your models here.

admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Ownership)
admin.site.register(Driving_license)