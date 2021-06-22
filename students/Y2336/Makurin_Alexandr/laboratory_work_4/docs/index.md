# Заключетельная работа курса по web-разработке на Django ФСПО ИТМО

## Модель

![image](https://user-images.githubusercontent.com/43097289/122927664-c4b69f80-d371-11eb-9386-711ae05b8b53.png)

## Django модели

```python
class Playground(models.Model):
    address = models.CharField(max_length=50)
    directorSurname = models.CharField(max_length=50)
    childrenPrice = models.FloatField()
    discountPrice = models.FloatField()
    adultPrice = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.directorSurname, self.address)


class Ride(models.Model):
    name = models.CharField(max_length=50)
    startDate = models.DateField(default=datetime.now())
    lifetime = models.BigIntegerField()
    basePrice = models.BigIntegerField()
    playground = models.ForeignKey('Playground', on_delete=models.CASCADE)

    db_constraints = {
        'price_rule': 'check (basePrice > 0)',
    }

    def __str__(self):
        return '%s' % self.name


class Usage(models.Model):
    day = models.DateField(default=datetime.now())
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE)
    childrenSales = models.BigIntegerField()
    discountSales = models.BigIntegerField()
    adultSales = models.BigIntegerField()

    def __str__(self):
        return '%s' % self.day
```

## Django URLs

```python
router = DefaultRouter()
router.register(r'rides', RideViewSet)
router.register(r'playgrounds', PlaygroundViewSet)
router.register(r'usages', UsageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
```

### /api/rides/

##### GET
Возвращает JSON массив с аттракционами

##### POST
Позволяет добавить новый аттракцион

##### Формат записи с аттракционом
```json
{
    "id": <id>,
    "name": <Название аттракциона>,
    "startDate": <Дата создания аттракциона>,
    "lifetime": <Время действия гарантии>,
    "basePrice": <Базовая цена за использование аттракциона>,
    "playground": <id площадки>
}
```

### /api/playgrounds/

##### GET
Возвращает JSON массив с парками аттракционов

##### POST
Позволяет добавить новый парк аттракционов

##### Формат записи с парком
```json
{
    "id": <id>,
    "address": <Местонахождение парка>,
    "directorSurname": <Директор парка>,
    "childrenPrice": <Модификатор цены аттракционов для детей>,
    "discountPrice": <Модификатор цены аттракционов для льготников>,
    "adultPrice": <Модификатор цены аттракционов для взрослых>
}
```

### /api/usages/

##### GET
Возвращает JSON массив с использованием аттракционов

##### POST
Позволяет добавить запись об использовании аттракциона

##### Формат записи об использовании аттракциона
```json
{
    "id": <id>,
    "day": <Дата в которую использовался аттракцион>,
    "ride": <id аттракциона>,
    "childrenSales": <Количество проданных детских билетов>,
    "discountSales": <Количество проданных льготных билетов>,
    "adultSales": <Количество проданных взрослых билетов>
}
```

## Front URLs

### /login

Вход

### /playgrounds

Список и редактирование парков аттракционов

### /rides

Список и редактирование аттракционов

### /usages

Список и редактирование использований аттракционов

### /registerUsage

Добавление использований аттракционов

### /registerRide

Добавление аттракционов

### /registerPlayground

Добавление парков аттракционов

