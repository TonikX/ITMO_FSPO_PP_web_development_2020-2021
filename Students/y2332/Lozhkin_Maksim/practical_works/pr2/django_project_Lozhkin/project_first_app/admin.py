from django.contrib import admin


from .models import *
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Ownership)
admin.site.register(DriverLicense)


