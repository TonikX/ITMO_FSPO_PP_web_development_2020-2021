from django.contrib import admin
from .models import auto, autoOwner, ownership, driverDocuments
# Register your models here.

admin.site.register(auto)
admin.site.register(autoOwner)
admin.site.register(ownership)
admin.site.register(driverDocuments)
