from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('User', 'User')],
        default='User'
    )
    bio = models.TextField(blank=True, null=True)

   
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
