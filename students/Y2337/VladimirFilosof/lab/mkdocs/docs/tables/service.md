# Service

## Код модели
```python
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField()
    preview = models.ImageField(upload_to='img/service/', max_length=255)
```
