import {HTTP} from "./common";

export const Lecturer = {
    create(data) {
        return HTTP.post('/lecturers/', data).then(response => {
            return response.data
        })
    },
    delete(lecturer) {
        return HTTP.delete(`/lecturers/${lecturer.id}/`)
    },
    list() {
        return HTTP.get('/lecturers/').then(response => {
            return response.data
        })
    },
    update(lecturer) {
        return HTTP.put(`/lecturers/${lecturer.data.id}/`, lecturer).then(response => {
            return response.data
        })
    }
}