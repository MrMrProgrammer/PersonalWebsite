from django.contrib import admin
from SiteSetting import models


class showHomeData(admin.ModelAdmin):
    list_display = ["__str__", 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


admin.site.register(models.HomeData, showHomeData)
