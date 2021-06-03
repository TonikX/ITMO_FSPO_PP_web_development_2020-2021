import axios from 'axios'

export const HTTP = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
    headers: {
        "Content-type": "application/json",
        // TODO авторизация
        "Authorization": "Token 364d9d9fa36a8554d9751215d746c22b6accdf51"
    }
})