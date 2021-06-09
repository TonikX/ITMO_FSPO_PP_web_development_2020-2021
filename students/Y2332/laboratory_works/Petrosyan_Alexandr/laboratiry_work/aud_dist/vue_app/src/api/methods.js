import {HTTP} from "./common";

export const Methods = {
    create(data, tableName) {
        return HTTP.post(`/${tableName}/`, data).then(response => {
            return response.data
        })
    },
    delete(item, tableName) {
        return HTTP.delete(`/${tableName}/${item.id}/`)
    },
    list(tableName) {
        return HTTP.get(`/${tableName}/`).then(response => {
            return response.data
        })
    },
    update(item, tableName) {
        return HTTP.put(`/${tableName}/${item.data.id}/`, item).then(response => {
            return response.data
        })
    }
}