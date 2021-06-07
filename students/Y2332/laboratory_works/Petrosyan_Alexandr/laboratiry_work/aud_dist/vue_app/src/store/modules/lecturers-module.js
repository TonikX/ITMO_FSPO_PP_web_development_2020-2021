import {Lecturer} from "../../api/lecturers"

export default {
    state: {
        lecturers: [],
    },
    getters: {
        lecturers: state => state.lecturers,
    },
    mutations: {
        ADD_LECTURER(state, lecturer) {
            state.lecturers.data.unshift(lecturer.data)
        },
        REMOVE_LECTURER(state, {id}) {
            let index = state.lecturers.data.findIndex(lecturer => lecturer.id === id)
            state.lecturers.data.splice(index, 1)
        },
        SET_LECTURERS(state, {lecturers}) {
            state.lecturers = lecturers
        },
    },
    actions: {
        createLecturer({commit}, lecturerData) {
            Lecturer.create(lecturerData).then(lecturer => {
                commit('ADD_LECTURER', lecturer)
            })
        },
        deleteLecturer({commit}, lecturer) {
            Lecturer.delete(lecturer).then(response => {
                commit('REMOVE_LECTURER', lecturer)
            })
        },
        getLecturers({commit}) {
            Lecturer.list().then(lecturers => {
                commit('SET_LECTURERS', {lecturers})
            })
        },
    },
};