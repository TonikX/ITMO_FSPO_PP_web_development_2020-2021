from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='img/projects/', max_length=255, null=True, blank=True)
    project_url = models.CharField(max_length=255, null=True, blank=True)
    code_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'id {self.id}: {self.title}'
