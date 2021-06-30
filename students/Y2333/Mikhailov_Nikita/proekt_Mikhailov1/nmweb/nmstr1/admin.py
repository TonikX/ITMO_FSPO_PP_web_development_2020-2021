from django.contrib import admin

# Register your models here.
from .models import Car_owner
from .models import Car
from .models import License
from .models import Possesion


admin.site.register(Car_owner)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Possesion)





