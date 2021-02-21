from django.contrib import admin
from .models import CarOwner
from .models import Ownership
from .models import DriverLicense
from .models import Car

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicense)

