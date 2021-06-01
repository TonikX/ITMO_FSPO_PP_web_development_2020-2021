import {_axios} from '../plugins/axios'

export const Lecturer = {
    create(config) {
        return _axios.post('/lecturers/', config).then(response => {
            return response.data
        })
    },
    delete(lecturer) {
        return _axios.delete(`/lecturers/${lecturer.id}`)
    },
    list() {
        return _axios.get('/lecturers/').then(response => {
            return response.data
        })
    }
}