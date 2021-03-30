from django.contrib import admin
from UP_app.models import CarOwner,Car,Ownership,DriverLicense

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicense)

# Register your models here.
