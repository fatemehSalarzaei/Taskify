# admin.py

from django.contrib import admin
from .models import Task
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'project', 'due_date', 'priority', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'assigned_to__username', 'project__title', 'status')
    list_filter = ('priority', 'status', 'assigned_to', 'project', 'due_date')

admin.site.register(Task, TaskAdmin)
