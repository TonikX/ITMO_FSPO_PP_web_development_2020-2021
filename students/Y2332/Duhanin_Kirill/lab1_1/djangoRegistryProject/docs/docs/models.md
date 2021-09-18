# Models
## Building
> Здание университета

- **list** `building/list` -- Список всех объектов
- **detail** `building/<int:pk>` -- Подробности об объекте с id = pk
- **create** `building/create` -- Создать объект
- **delete** `building/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `building/<int:pk>/update` -- Обновление данных объекта с id = pk
## Department
> Подразделение университета (деканат, кафедра, вычислительный центр)

- **list** `department/list` -- Список всех объектов
- **detail** `department/<int:pk>` -- Подробности об объекте с id = pk
- **create** `department/create` -- Создать объект
- **delete** `department/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `department/<int:pk>/update` -- Обновление данных объекта с id = pk
## Worker
> Работник университета. Может руководить подразделением или нести ответственность за аудиторию 

- **list** `worker/list` -- Список всех объектов
- **detail** `worker/<int:pk>` -- Подробности об объекте с id = pk
- **create** `worker/create` -- Создать объект
- **delete** `worker/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `worker/<int:pk>/update` -- Обновление данных объекта с id = pk
## Management
> Управление выражавет зависимость между работником и подразделением

- **list** `management/list` -- Список всех объектов
- **detail** `management/<int:pk>` -- Подробности об объекте с id = pk
- **create** `management/create` -- Создать объект
- **delete** `management/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `management/<int:pk>/update` -- Обновление данных объекта с id = pk
## Hall
> Аудитория закреплена за подразделением. Может быть компьютерным классом, актовым залом или лекционной аудитоией

- **list** `hall/list` -- Список всех объектов
- **detail** `hall/<int:pk>` -- Подробности об объекте с id = pk
- **create** `hall/create` -- Создать объект
- **delete** `hall/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `hall/<int:pk>/update` -- Обновление данных объекта с id = pk
## Responsibility
> Ответственность работника за аудиторией

- **list** `responsibility/list` -- Список всех объектов
- **detail** `responsibility/<int:pk>` -- Подробности об объекте с id = pk
- **create** `responsibility/create` -- Создать объект
- **delete** `responsibility/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `responsibility/<int:pk>/update` -- Обновление данных объекта с id = pk
## Property
> Словарь, содержащий список стандартных кодов

- **list** `property/list` -- Список всех объектов
- **detail** `property/<int:pk>` -- Подробности об объекте с id = pk
- **create** `property/create` -- Создать объект
- **delete** `property/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `property/<int:pk>/update` -- Обновление данных объекта с id = pk
## Unit
> Единица имущества закреплена за аудиторией посредством сущности Consist

- **list** `unit/list` -- Список всех объектов
- **detail** `unit/<int:pk>` -- Подробности об объекте с id = pk
- **create** `unit/create` -- Создать объект
- **delete** `unit/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `unit/<int:pk>/update` -- Обновление данных объекта с id = pk
## Consist
> Содержание связывает аудиторию и единицу имущества 

- **list** `consist/list` -- Список всех объектов
- **detail** `consist/<int:pk>` -- Подробности об объекте с id = pk
- **create** `consist/create` -- Создать объект
- **delete** `consist/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `consist/<int:pk>/update` -- Обновление данных объекта с id = pk
## Revaluation
> Переоценка 

- **list** `revaluation/list` -- Список всех объектов
- **detail** `revaluation/<int:pk>` -- Подробности об объекте с id = pk
- **create** `revaluation/create` -- Создать объект
- **delete** `revaluation/<int:pk>/delete` -- Удалить объект с id = pk
- **update** `revaluation/<int:pk>/update` -- Обновление данных объекта с id = pk