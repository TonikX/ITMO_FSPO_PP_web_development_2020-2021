from django.contrib import admin
from .models import Owner
from .models import DriversLicense
from .models import Car
from .models import CarOwner



# Register your models here.


admin.site.register(Owner)


admin.site.register(DriversLicense)


admin.site.register(Car)


admin.site.register(CarOwner)
