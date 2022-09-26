# Карта сайта
Структура URL адресов клиентской и серверной части 

# Клиентская часть

## Авторизация

* `/login` 

## Главная страница

* `/home` 

## Таблицы

* `/schedule` Расписание
* `/lecturers` Преподаватели
* `/disciplines` Дисциплины
* `/audiences` Аудитории
* `/groups` Группы


# Серверная часть

## Администрирование
* `/admin` Админ панель

## API
### Авторизация
* `/auth/token/login` `POST` Вход в систему
* `/auth/token/logout` `POST` Выход
* `/auth/users/` Список пользователей
### Сущности

Доступные методы списков: `GET, POST, HEAD, OPTIONS`

* `/api/disciplines/`  Список дисциплин
* `/api/lecturers/` Список преподавателей
* `/api/groups/` Список групп
* `/api/audiences/` Список аудиторий
* `/api/schedules/` Расписание

Доступные методы экземпляров: `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

* `/api/disciplines/<id>` Экземпляр дисциплины
* `/api/lecturers/<id>` Экземпляр преподавателя
* `/api/groups/<id>` Экземпляр группы
* `/api/audiences/<id>` Экземпляр аудитории
* `/api/schedules/<id>` Экземпляр расписания