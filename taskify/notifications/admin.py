
from django.contrib import admin
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read', 'created_at', 'user')

admin.site.register(Notification, NotificationAdmin)
