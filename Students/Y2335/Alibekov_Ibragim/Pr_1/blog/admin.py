from django.contrib import admin
from .models import Owner, Car, Possession, License

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Possession)
admin.site.register(License)
