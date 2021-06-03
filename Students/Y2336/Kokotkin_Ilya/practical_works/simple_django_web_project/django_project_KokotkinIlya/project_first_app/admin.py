from django.contrib import admin

from .models import Owner, License, Auto, Ownership

admin.site.register(Owner)
admin.site.register(License)
admin.site.register(Auto)
admin.site.register(Ownership)

# Register your models here.