#Urls Backend
```python
#Админ панель
admin/
#Авторизация
auth/

#Все кузова
bodies/
#Поиск по кузовам
bodies?s=something
#Детали кузова
bodies/<int:pk>/

#Все двигатели
engines/
#Поиск по двигателям
engines?s=something
#Детали двигателя
engines/<int:pk>/

#Все модели
models/
#Поиск по моделям
models?s=something
#Детали модели
models/<int:pk>/

#Все юридические владельцы
legal_owners/
#Поиск по юридическим владельцам
legal_owners?s=something
#Детали юридического владельца
legal_owners/<int:pk>/

#Все физические владельцы
physical_owners/
#Поиск по физическим владельцам
physical_owners?s=something
#Детали физического владельца
physical_owners/<int:pk>/

#Все автомобили
cars/
#Поиск по автомобилям
cars?s=something
#Детали автомобиля
cars/<int:pk>/

#Все угоны
drive_away_info_list/
#Поиск по угонам
drive_away_info_list?s=something
#Детали автомобиля
drive_away_info_list/<int:pk>/

#Все инспекторы
inspectors/
#Поиск по инеспекторам
inspectors?s=something
#Детали инспектора
inspectors/<int:pk>/

#Все техосмотры
watch_info_list/
#Поиск по техосмотрам
watch_info_list?s=something
#Детали инспектора
watch_info_list/<int:pk>/
```