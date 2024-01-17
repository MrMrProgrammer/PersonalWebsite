from django.contrib import admin
from . import models


class showLogs(admin.ModelAdmin):
    list_display = ["ip", "date", "time", "agent", "language"]


admin.site.register(models.Logger, showLogs)