from django.contrib import admin

from .models import CarOwner

admin.site.register(CarOwner)

from .models import Car

admin.site.register(Car)

from .models import possession

admin.site.register(possession)

from .models import driverID

admin.site.register(driverID)

# Register your models here.
