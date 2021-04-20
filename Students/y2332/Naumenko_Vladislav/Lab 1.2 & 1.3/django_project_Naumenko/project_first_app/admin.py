from django.contrib import admin
from .models import Owner, DriversLicense, Auto, AutoOwner

# Register your models here.

admin.site.register(Owner)
admin.site.register(DriversLicense)
admin.site.register(Auto)
admin.site.register(AutoOwner)
