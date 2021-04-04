from django.contrib import admin

from .models import CarOwner
from .models import Car
from .models import OwnerShip
from .models import DriverLicense

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(OwnerShip)
admin.site.register(DriverLicense)
