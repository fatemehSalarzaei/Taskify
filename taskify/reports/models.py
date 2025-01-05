from django.db import models
from projects.models import Project

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
