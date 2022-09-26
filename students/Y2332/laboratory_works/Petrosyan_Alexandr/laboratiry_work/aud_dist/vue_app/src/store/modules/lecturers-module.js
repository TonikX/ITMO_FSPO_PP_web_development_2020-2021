import {Methods} from "../../api/methods";

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
        UPDATE_LECTURER(state, lecturer) {
            let index = state.lecturers.data.findIndex(l => l.id === lecturer.data.id)
            state.lecturers.data.splice(index, 1)
            state.lecturers.data.unshift(lecturer.data)
        }
    },
    actions: {
        createLecturer({commit}, lecturerData) {
            Methods.create(lecturerData, 'lecturers').then(lecturer => {
                commit('ADD_LECTURER', lecturer)
            })
        },
        deleteLecturer({commit}, lecturer) {
            Methods.delete(lecturer, 'lecturers').then(() => {
                commit('REMOVE_LECTURER', lecturer)
            })
        },
        getLecturers({commit}) {
            Methods.list('lecturers').then(lecturers => {
                commit('SET_LECTURERS', {lecturers})
            })
        },
        updateLecturer({commit}, lecturer){
            Methods.update(lecturer, 'lecturers').then(lecturer => {
                commit('UPDATE_LECTURER', lecturer)
            })
        }
    },
};