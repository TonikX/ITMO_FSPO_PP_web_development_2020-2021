from django.contrib import admin
from .models import User, Car, DriversLicense, Owning

# Register your models here.
admin.site.register(User)
admin.site.register(Car)
admin.site.register(DriversLicense)
admin.site.register(Owning)
