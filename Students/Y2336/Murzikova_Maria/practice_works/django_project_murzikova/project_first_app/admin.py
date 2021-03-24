from django.contrib import admin

from .models import Owner
admin.site.register(Owner)

from .models import Car
admin.site.register(Car)

from .models import Hold
admin.site.register(Hold)

from .models import License
admin.site.register(License)
