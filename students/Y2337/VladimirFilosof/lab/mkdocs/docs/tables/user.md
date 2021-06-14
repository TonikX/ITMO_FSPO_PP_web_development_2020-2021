# User

## Код модели
```python
class User(AbstractUser):
    orders = models.ManyToManyField(Service, through=Order)
```
