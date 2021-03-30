from django.contrib import admin

from .models import CarOwner
admin.site.register(CarOwner)

from .models import Car
admin.site.register(Car)

from .models import Owning
admin.site.register(Owning)

from .models import License
admin.site.register(License)