from django.contrib import admin
from .models import Owner, Car, License, Owning

# Register your models here.
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Owning)


