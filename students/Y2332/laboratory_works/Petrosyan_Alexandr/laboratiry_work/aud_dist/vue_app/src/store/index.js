import Vue from 'vue'
import Vuex from 'vuex'
import './mutation-types'
import {ADD_LECTURER, REMOVE_LECTURER, SET_LECTURERS} from "./mutation-types";
import {Lecturer} from "../api/lecturers";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        lecturers: []
    },
    getters: {
        // получение списков из состояний
        lecturers: state => state.lecturers
    },
    mutations: {
        [ADD_LECTURER](state, lecturer) {
            state.lecturers = [lecturer, ...state.lecturers]
        },
        [REMOVE_LECTURER](state, {id}) {
            state.lecturers = state.lecturers.filter(lecturer => {
                return lecturer.id !== id
            })
        },
        [SET_LECTURERS](state, {lecturers}) {
            state.lecturers = lecturers
        }
    },
    actions: {
        createLecturer({commit}, lecturerData) {
            Lecturer.create(lecturerData).then(lecturer => {
                commit(ADD_LECTURER, lecturer)
            })
        },
        deleteLecturer({commit}, lecturer) {
            Lecturer.delete(lecturer).then(response => {
                commit(REMOVE_LECTURER, lecturer)
            })
        },
        getLecturers({commit}) {
            Lecturer.list().then(lecturers => {
                commit(SET_LECTURERS, {lecturers})
            })
        }
    },
    modules: {}
})
