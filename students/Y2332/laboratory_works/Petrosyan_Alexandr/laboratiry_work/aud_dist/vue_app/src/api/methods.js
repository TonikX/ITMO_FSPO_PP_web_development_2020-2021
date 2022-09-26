import {HTTP} from "./common";

export const Methods = {
    create(data, tableName) {
        return HTTP.post(`/api/${tableName}/`, data).then(response => {
            return response.data
        })
    },
    delete(item, tableName) {
        return HTTP.delete(`/api/${tableName}/${item.id}/`)
    },
    list(tableName) {
        return HTTP.get(`/api/${tableName}/`).then(response => {
            return response.data
        })
    },
    update(item, tableName) {
        return HTTP.put(`/api/${tableName}/${item.data.id}/`, item).then(response => {
            return response.data
        })
    },
    login(data) {
        return HTTP.post('/auth/token/login/', data).then(response => {
            return response.data
        })
    },
    logout() {
        return HTTP.post('/auth/token/logout/').then(response => {
            return response.data
        })
    }
}