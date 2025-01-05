# admin.py

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'bio', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'role')
    ordering = ('date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'groups', 'user_permissions')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
