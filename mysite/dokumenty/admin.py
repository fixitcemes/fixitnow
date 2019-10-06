from django.contrib import admin
from .models import CrashReport, Author, Occupation, Device, DeviceType

admin.site.register(CrashReport)
admin.site.register(Author)
admin.site.register(Occupation)
admin.site.register(Device)
admin.site.register(DeviceType)