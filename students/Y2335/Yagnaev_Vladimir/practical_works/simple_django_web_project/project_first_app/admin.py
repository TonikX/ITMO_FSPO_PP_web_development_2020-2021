from django.contrib import admin
from .models import owner
from .models import car
from .models import ownership
from .models import license

admin.site.register(owner)
admin.site.register(car)
admin.site.register(ownership)
admin.site.register(license)
# Register your models here.
