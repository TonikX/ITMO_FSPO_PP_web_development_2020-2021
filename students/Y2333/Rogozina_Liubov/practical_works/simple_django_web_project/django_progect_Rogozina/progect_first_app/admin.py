from django.contrib import admin

# Register your models here.
from .models import Car_owner
from .models import Car
from .models import Driver_license
from .models import Ownership
admin.site.register(Car_owner)
admin.site.register(Car)
admin.site.register(Driver_license)
admin.site.register(Ownership)
