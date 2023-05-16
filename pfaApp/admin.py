from django.contrib import admin

# Register your models here.

from pfaApp.models import BPM, PRESSION, Temp, RegiUser
admin.site.register(BPM)
admin.site.register(PRESSION)
admin.site.register(Temp)
admin.site.register(RegiUser)
