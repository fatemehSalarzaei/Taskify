
from django.contrib import admin
from .models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_by', 'get_team_members')
    search_fields = ('title', 'description', 'created_by__username')
    list_filter = ('start_date', 'end_date', 'created_by')

    def get_team_members(self, obj):
        return ", ".join([member.username for member in obj.team_members.all()])
    get_team_members.short_description = 'Team Members'

admin.site.register(Project, ProjectAdmin)
