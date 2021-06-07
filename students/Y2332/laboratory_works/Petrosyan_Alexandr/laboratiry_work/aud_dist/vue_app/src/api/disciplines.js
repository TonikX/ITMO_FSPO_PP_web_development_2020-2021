import {HTTP} from "./common";

export const Discipline = {
    create(config) {
        return HTTP.post('/disciplines/', config).then(response => {
            return response.data
        })
    },
    delete(discipline) {
        return HTTP.delete(`/disciplines/${discipline.id}/`)
    },
    list() {
        return HTTP.get('/disciplines/').then(response => {
            return response.data
        })
    }
}