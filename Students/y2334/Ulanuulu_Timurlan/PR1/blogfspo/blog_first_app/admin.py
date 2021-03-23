from django.contrib import admin
from .models import Owner, DriversLicense, car, possession
admin.site.register(Owner)
admin.site.register(DriversLicense)
admin.site.register(car)
admin.site.register(possession)
# Register your models here.
