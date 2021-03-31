from django.contrib import admin
from .models import Car, CarOwnership, CarOwner, DrivingLicense

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(CarOwnership)
class CarOwnershipAdmin(admin.ModelAdmin):
    pass

@admin.register(CarOwner)
class CarOwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(DrivingLicense)
class DrivingLicenseAdmin(admin.ModelAdmin):
    pass
