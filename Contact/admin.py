from django.contrib import admin
from . import models


class showContact(admin.ModelAdmin):
    list_display = ["full_name", 'email', 'phone_number', 'message', 'formatted_datetime']

    def formatted_datetime(self, obj):
        return obj.datetime.strftime('%Y-%m-%d | %H:%M')

    formatted_datetime.short_description = 'Date & Time'

admin.site.register(models.Contact, showContact)
