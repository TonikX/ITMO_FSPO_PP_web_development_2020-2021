from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Discipline)
admin.site.register(Lecturer)
admin.site.register(Group)
admin.site.register(Audience)
admin.site.register(Schedule)
