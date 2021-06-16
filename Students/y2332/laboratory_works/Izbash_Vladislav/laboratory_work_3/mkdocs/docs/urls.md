# Доступные URL

## Основные
* `/` - перенаправляет на веб-приложение ELibrary
* `/admin` - панель администрации Django

## REST API
URL данной категории имеют префикс `/api`

#### Работа с сущностями:
- `/api/authors/` и `/api/authors/{id}/` - работа с авторами
- `/api/book_copies/` и `/api/book_copies/{id}/` - работа с экземплярами книг
- `/api/book_revs/` и `/api/book_revs/{id}/` - работа с изданиями книг
- `/api/books/` и `/api/books/{id}/` - работа с книгами
- `/api/borrowers/` и `/api/borrowers/{id}/` - работа с читателями
- `/api/borrows/` и `/api/borrows/{id}/` - управление выдачами
- `/api/compilers/` и `/api/compilers/{id}/` - работа с составителями
- `/api/publishers/` и `/api/publishers/{id}/` - работа с издателями
- `/api/translators/` и `/api/translators/{id}/` - работа с переводчиками
- `/api/users/` и `/api/users/{id}/` - работа с пользователями
#### Авторизация
- `/api/token/login/` - получение токена по логину и паролю
- `/api/token/logout` - выход и отзыв токена

Более подробную информацию можно получить на `/api/docs`
