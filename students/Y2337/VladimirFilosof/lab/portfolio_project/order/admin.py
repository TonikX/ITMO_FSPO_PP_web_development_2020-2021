from django.contrib import admin
from django.contrib.admin import ModelAdmin

from order.models import User, Order, Service


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    pass
