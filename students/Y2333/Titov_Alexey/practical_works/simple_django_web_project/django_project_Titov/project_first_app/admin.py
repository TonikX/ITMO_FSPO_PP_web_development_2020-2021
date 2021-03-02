from django.contrib import admin
from .models import Car
from .models import Owner
from .models import CarOwning
from .models import DriverLicense


# Register your models here.


admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(CarOwning)
admin.site.register(DriverLicense)
