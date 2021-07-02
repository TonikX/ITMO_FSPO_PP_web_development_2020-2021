from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(PostOffice)
admin.site.register(EditorialOffice)
admin.site.register(Newspaper)
admin.site.register(PrintingOffice)
admin.site.register(Release)
admin.site.register(Article)
admin.site.register(Correction)
admin.site.register(NewspaperDistribution)