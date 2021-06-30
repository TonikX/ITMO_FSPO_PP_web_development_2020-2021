from django.contrib import admin

# Register your models here.

from .models import Resident
from .models import Hostel
from .models import Check_in_out
from .models import Room
from .models import Address
from .models import Payment
from .models import Organizatoin

admin.site.register(Resident)
admin.site.register(Hostel)
admin.site.register(Check_in_out)
admin.site.register(Room)
admin.site.register(Payment)
admin.site.register(Address)
admin.site.register(Organizatoin)
