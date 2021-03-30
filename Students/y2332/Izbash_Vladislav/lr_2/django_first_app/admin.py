from django.contrib import admin
from .models import CarOwner, Car, Ownership, User

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(User)