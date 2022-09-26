import axios from 'axios'

if (localStorage.getItem("auth_token")) {
    axios.defaults.headers.common['Authorization'] =
        "Token " + localStorage.getItem("auth_token")
}

export const HTTP = axios.create({
    baseURL: "http://127.0.0.1:8000/",
    headers: {
        "Content-type": "application/vnd.api+json",
    }
})