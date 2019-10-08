from django.contrib import admin
from .models import CrashReport, Author, Occupation, Device, DeviceType


#admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'employed_science')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


@admin.register(CrashReport)
class CrashReportsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Occupation)
admin.site.register(Device)
admin.site.register(DeviceType)

