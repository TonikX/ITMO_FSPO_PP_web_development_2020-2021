from django.contrib import admin

from .models import Car, Ownership
from django.contrib.auth import get_user_model
CarOwner = get_user_model()


admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
