from django.contrib import admin
from . import models


class showLogs(admin.ModelAdmin):
    list_display = ["ip", "count", "date", "time", "agent", "language", "client_name"]


admin.site.register(models.Logger, showLogs)
