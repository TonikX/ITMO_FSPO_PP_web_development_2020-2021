from django.contrib import admin

# Register your models here.


from .models import Car
from .models import CarOwner
from .models import Own
from .models import Doc

admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(Own)
admin.site.register(Doc)
