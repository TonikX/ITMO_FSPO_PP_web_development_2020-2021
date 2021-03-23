from django.contrib import admin
from .models import CarOwner, Car, Own


admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Own)