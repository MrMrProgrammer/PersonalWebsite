from django.contrib import admin
from . import models


class showContact(admin.ModelAdmin):
    list_display = ["full_name", 'email', 'phone_number', 'message', 'datetime']


admin.site.register(models.Contact, showContact)
