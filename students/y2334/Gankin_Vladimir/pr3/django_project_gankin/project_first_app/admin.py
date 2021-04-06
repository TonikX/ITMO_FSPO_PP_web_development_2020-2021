from django.contrib import admin

# Register your models here.
from .models import AutoOwner, Auto, Owning, DriverLicense

admin.site.register(AutoOwner)
admin.site.register(Auto)
admin.site.register(Owning)
admin.site.register(DriverLicense)
