from django.contrib import admin
from .models import Doctor
from .models import Service
from .models import DoctorService
from .models import Client
from .models import Ticket


admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(DoctorService)
admin.site.register(Client)
admin.site.register(Ticket)
