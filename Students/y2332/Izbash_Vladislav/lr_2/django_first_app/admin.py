from django.contrib import admin
from .models import CarOwner, Car, Ownership

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)