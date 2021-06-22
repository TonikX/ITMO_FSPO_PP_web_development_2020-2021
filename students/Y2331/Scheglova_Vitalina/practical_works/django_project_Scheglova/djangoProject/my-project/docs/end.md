# Endpoints

## /plane/list2
`/plane/list2` - Просмотр списка самолетов

- Метод: GET - получить список самолетов

## /plane_detail/int:plane_type_id/
` /plane_detail/int:plane_type_id/` - Получение данных о самолете

- Метод: GET - получить данные о самолете

##/plane/create
`/plane/create` - Создание самолета

- Метод: GET - получить список самолетов
- Метод: POST - создание самолетов;
request: {model_name, manufacturer, capacity}

##/clients/list2
`/clients/list2` - Просмотр списка клиентов

- Метод: GET - получить список клиентов

##/client/create
`/client/create` - Создание клиента

- Метод: GET - получить список клиентов
- Метод: POST - создание клиента
request: FIO_client, passport_number, date_of_passport_start, registration_number, who_give_the_passport)

##client_detail/int:client_id/
` client_detail/int:client_id/` - Получение данных о клиенте

- Метод: GET - получить данные о клиента

##/ticket_office/list2
`/ticket_office/list2` - Просмотр списка билетных офисов

- Метод: GET - получить список билетных офисов

##ticket_office_detail/int:ticket_office_id/
` ticket_office_detail/int:ticket_office_id/` - Получение данных о билетном офисе

- Метод: GET - получить данные о билетном офисе
##ticket_office/create
`ticket_office/create` - Создание билетного офиса

- Метод: GET - получить список билетных офисов
- Метод: POST - создание билетного офиса
request: ticket_office_adress)







