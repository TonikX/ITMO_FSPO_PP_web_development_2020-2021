from django.contrib import admin
from .models import auto
from .models import autoOwner
from .models import ownership
from .models import driverDocuments
# Register your models here.

admin.site.register(auto)
admin.site.register(autoOwner)
admin.site.register(ownership)
admin.site.register(driverDocuments)