from django.contrib import admin
from django.contrib.admin import ModelAdmin

from autobase_app.models import Driver, Waybill, Fuel, Car, Garage, MotorDepot, Refuel


@admin.register(Driver)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(MotorDepot)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Garage)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Car)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Fuel)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Refuel)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Waybill)
class ProjectAdmin(ModelAdmin):
    pass
