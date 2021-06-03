import {HTTP} from "./common";

export const Lecturer = {
    create(config) {
        return HTTP.post('/lecturers/', config).then(response => {
            return response.data
        })
    },
    delete(lecturer) {
        return HTTP.delete(`/lecturers/${lecturer.id}`)
    },
    list() {
        return HTTP.get('/lecturers/').then(response => {
            return response.data
        })
    }
}