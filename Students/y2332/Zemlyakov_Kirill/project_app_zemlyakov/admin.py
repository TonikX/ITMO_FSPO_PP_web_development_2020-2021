from django.contrib import admin
from .models import CarOwner,Car,DriverLicense,Ownership
admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(Ownership)
# Register your models here.
