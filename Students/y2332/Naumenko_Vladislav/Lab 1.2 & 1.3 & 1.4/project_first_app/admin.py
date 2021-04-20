from django.contrib import admin
from .models import DriversLicense, Auto, AutoOwner
from django.contrib.auth import get_user_model
Owner = get_user_model()

# # Register your models here.

admin.site.register(Owner)
admin.site.register(DriversLicense)
admin.site.register(Auto)
admin.site.register(AutoOwner)
