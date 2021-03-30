from django.contrib import admin
from .models import CarOwner
admin.site.register(CarOwner)

from .models import Car
admin.site.register(Car)

from .models import OwnerShip
admin.site.register(OwnerShip)

from .models import DrivingLicense
admin.site.register(DrivingLicense)


