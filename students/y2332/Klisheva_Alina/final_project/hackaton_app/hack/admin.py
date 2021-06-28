from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(User)
admin.site.register(TeamMember)
admin.site.register(Issue)
admin.site.register(Solution)

