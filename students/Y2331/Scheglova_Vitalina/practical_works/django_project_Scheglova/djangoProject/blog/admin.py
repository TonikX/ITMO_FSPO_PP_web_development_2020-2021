from django.contrib import admin

from .models import Plane_type, Plane, Client, Ticket_office, Cashier, Ticket, Order, Flight, Transit_boarding, Staff, Crew
admin.site.register(Plane_type)
admin.site.register(Plane)
admin.site.register(Client)
admin.site.register(Ticket_office)
admin.site.register(Cashier)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(Flight)
admin.site.register(Transit_boarding)
admin.site.register(Staff)
admin.site.register(Crew)
