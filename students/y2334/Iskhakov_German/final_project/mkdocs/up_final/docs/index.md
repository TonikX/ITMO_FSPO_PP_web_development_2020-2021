# Calories calculator project

## REST API

### 1. Выход из аккаунта

address: /api/exit

method: POST 

```
req: {
    signedCookie?: token
}
```

```
res: void
```

### 2. Получение информации о пользователе

address: /api/getMe

method: GET 

```
req: {
    signedCookie?: token
}
```

```
res: {
    name, 
    surname, 
    age, 
    height, 
    weight, 
    sex
}
```

### 3. Получение информации о блюдах пользователя

address: /api/getMeals

method: GET 

```
req: {
    signedCookie?: token
}
```

```
res: {
    status: 'success',
    meals: [{
        type,
        name,
        cal
    }]
}
```

```
error: {
    status: 'error',
    message
}
```

### 3. Добавление блюда пользователя

address: /api/registerMeal

method: POST 

```
req: {
    signedCookie?: token
}
```

```
res: {
    status: 'success'
}
```

```
error: {
    status: 'error',
    message
}
```

### 4. Обновление данных пользователя

address: /api/updateUser

method: POST 

```
req: {
    signedCookie?: token
}
```

```
res: {
    status: 'success'
}
```

```
error: {
    status: 'error',
    message
}
```

### 5. Авторизация пользователя

address: /api/logUser

method: POST 

```
req: {
    signedCookie?: token
}
```

```
res: {
    status: 'success'
}
```

```
error: {
    status: 'error',
    message
}
```

### 6. Регистрация пользователя

address: /api/createUser

method: POST 

```
req: {
    signedCookie?: token
}
```

```
res: {
    status: 'success'
}
```

```
error: {
    status: 'error',
    message
}
```