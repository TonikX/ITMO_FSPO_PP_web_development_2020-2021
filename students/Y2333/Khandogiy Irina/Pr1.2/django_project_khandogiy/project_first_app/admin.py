from django.contrib import admin

from .models import CarOwner

# Register your models here.

admin.site.register(CarOwner)


from .models import DriverLicense


admin.site.register(DriverLicense)

from .models import Car

admin.site.register(Car)

from .models import Own

admin.site.register(Own)
