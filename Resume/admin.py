from django.contrib import admin
from . import models


class showSkill(admin.ModelAdmin):
    list_display = ["skill_name", 'priority', 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


class showLanguage(admin.ModelAdmin):
    list_display = ["language", 'priority', 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


class showExperience(admin.ModelAdmin):
    list_display = ["__str__", 'from_date', 'end_date', 'is_present', 'job_title', 'location', 'content', 'is_active']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


class showEducation(admin.ModelAdmin):
    list_display = ["__str__", 'is_active', 'from_date', 'end_date', 'is_present', 'grade', 'description']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


class showResumeFile(admin.ModelAdmin):
    list_display = ["datetime", 'is_active', 'file']
    list_filter = ["is_active"]
    list_editable = ["is_active"]


admin.site.register(models.Skill, showSkill)
admin.site.register(models.Language, showLanguage)
admin.site.register(models.Experience, showExperience)
admin.site.register(models.Education, showEducation)
admin.site.register(models.ResumeFile, showResumeFile)
