from django.contrib import admin
from .models import License
from .models import Car
from .models import OwnerShip
from .models import CarOwner

# Register your models here.
admin.site.register(CarOwner)
admin.site.register(OwnerShip)
admin.site.register(Car)
admin.site.register(License)
