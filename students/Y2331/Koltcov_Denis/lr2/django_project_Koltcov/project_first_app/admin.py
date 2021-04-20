from django.contrib import admin

from .models import Car, CarOwner, License, Ownership
admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(License)
admin.site.register(Ownership)

# Register your models here.
