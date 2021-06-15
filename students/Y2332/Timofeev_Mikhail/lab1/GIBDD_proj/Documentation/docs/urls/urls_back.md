#Urls Backend
```python
#Админ панель
admin/
#Авторизация
auth/

#Все кузова
^bodies/$ [name='body-list']
#Поиск по кузовам
^bodies\.(?P<format>[a-z0-9]+)/?$ [name='body-list']
#Детали кузова
^bodies/(?P<pk>[^/.]+)/$ [name='body-detail']

#Все двигатели
^engines/$ [name='engine-list']
#Поиск по двигателям
^engines\.(?P<format>[a-z0-9]+)/?$ [name='engine-list']
#Детали двигателя
^engines/(?P<pk>[^/.]+)/$ [name='engine-detail']

#Все модели
^models/$ [name='model-list']
#Поиск по моделям
^models\.(?P<format>[a-z0-9]+)/?$ [name='model-list']
#Детали модели
^models/(?P<pk>[^/.]+)/$ [name='model-detail']

#Все юридические владельцы
^legal_owners/$ [name='legal_owner-list']
#Поиск по юридическим владельцам
^legal_owners\.(?P<format>[a-z0-9]+)/?$ [name='legal_owner-list']
#Детали юридического владельца
^legal_owners/(?P<pk>[^/.]+)/$ [name='legal_owner-detail']

#Все физические владельцы
^physical_owners/$ [name='physical_owner-list']
#Поиск по физическим владельцам
^physical_owners\.(?P<format>[a-z0-9]+)/?$ [name='physical_owner-list']
#Детали физического владельца
^physical_owners/(?P<pk>[^/.]+)/$ [name='physical_owner-detail']

#Все автомобили
^cars/$ [name='car-list']
#Поиск по автомобилям
^cars\.(?P<format>[a-z0-9]+)/?$ [name='car-list']
#Детали автомобиля
^cars/(?P<pk>[^/.]+)/$ [name='car-detail']

#Все угоны
^drive_away_info_list/$ [name='drive_away_info-list']
#Поиск по угонам
^drive_away_info_list\.(?P<format>[a-z0-9]+)/?$ [name='drive_away_info-list']
#Детали автомобиля
^drive_away_info_list/(?P<pk>[^/.]+)/$ [name='drive_away_info-detail']

#Все инспекторы
^inspectors/$ [name='inspector-list']
#Поиск по инеспекторам
^inspectors\.(?P<format>[a-z0-9]+)/?$ [name='inspector-list']
#Детали инспектора
^inspectors/(?P<pk>[^/.]+)/$ [name='inspector-detail']

#Все техосмотры
^watch_info_list/$ [name='watch_info-list']
#Поиск по техосмотрам
^watch_info_list\.(?P<format>[a-z0-9]+)/?$ [name='watch_info-list']
#Детали инспектора
^watch_info_list/(?P<pk>[^/.]+)/$ [name='watch_info-detail']
^watch_info_list/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='watch_info-detail']
```