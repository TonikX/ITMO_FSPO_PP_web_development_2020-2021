from django.contrib import admin

from .models import Car, Ownership, CarOwner

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
