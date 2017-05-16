from django.contrib import admin
from .models import AV, Device_Types
# Register your models here.

class AVAdmin(admin.ModelAdmin):
    list_display = ('hostname','ip_address','action','dat_version','date_rec',)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device',)

admin.site.register(AV, AVAdmin)
admin.site.register(Device_Types, DeviceAdmin)