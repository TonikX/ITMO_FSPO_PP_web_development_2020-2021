from django.contrib import admin

from .models import CarOwner
from .models import Car
from .models import Own
from .models import Doc

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Own)
admin.site.register(Doc)

# Register your models here.
