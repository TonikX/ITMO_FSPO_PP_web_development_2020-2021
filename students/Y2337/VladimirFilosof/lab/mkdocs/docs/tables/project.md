### Project

# Код модели
```python
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='img/projects/', max_length=255, null=True, blank=True)
    project_url = models.CharField(max_length=255, null=True, blank=True)
    code_url = models.CharField(max_length=255, null=True, blank=True)
```
