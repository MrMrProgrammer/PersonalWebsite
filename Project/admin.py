from django.contrib import admin
from . import models


class showProject(admin.ModelAdmin):
    list_display = ["project_name", 'description', 'project_image', 'link', 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


admin.site.register(models.Project, showProject)
