from django.contrib import admin
from .models import Repair, Schedule_works, RepairBrigade, Worker, Wagon


class RepairAdmin(admin.ModelAdmin):
    pass


admin.site.register(Worker, RepairAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(Schedule_works, RepairAdmin)
admin.site.register(RepairBrigade, RepairAdmin)
admin.site.register(Wagon, RepairAdmin)
