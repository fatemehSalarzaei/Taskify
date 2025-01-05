
from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'project__title')
    list_filter = ('created_at', 'updated_at', 'project')

admin.site.register(Report, ReportAdmin)
