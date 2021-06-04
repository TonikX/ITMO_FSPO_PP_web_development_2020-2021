import axios from 'axios'

axios.defaults.headers.common['Authorization'] = "Token " + localStorage.getItem("auth_token");

export const HTTP = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
    headers: {
        "Content-type": "application/json",
    }
})