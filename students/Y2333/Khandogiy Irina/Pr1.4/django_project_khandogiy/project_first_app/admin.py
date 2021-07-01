from django.contrib import admin
from .models import CarOwner
from .models import DriverLicense
from .models import Car
from .models import Own

admin.site.register(CarOwner)


admin.site.register(DriverLicense)


admin.site.register(Car)


admin.site.register(Own)


