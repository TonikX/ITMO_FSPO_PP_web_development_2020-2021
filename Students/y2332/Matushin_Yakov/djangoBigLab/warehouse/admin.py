from django.contrib import admin
from .models import Employer, Client, Supplier, Production, Batch

admin.site.register(Employer)
admin.site.register(Client)
admin.site.register(Supplier)
admin.site.register(Production)
admin.site.register(Batch)

# Register your models here.
