import {Methods} from "../../api/methods";


export default {
    state: {
        disciplines: []
    },
    getters: {
        disciplines: state => state.disciplines
    },
    mutations: {
        ADD_DISCIPLINE(state, discipline) {
            state.disciplines.data.unshift(discipline.data)
        },
        REMOVE_DISCIPLINE(state, {id}) {
            let index = state.disciplines.data.findIndex(discipline => discipline.id === id)
            state.disciplines.data.splice(index, 1)
        },
        SET_DISCIPLINES(state, {disciplines}) {
            state.disciplines = disciplines
        },
        UPDATE_DISCIPLINE(state, discipline) {
            let index = state.disciplines.data.findIndex(d => d.id === discipline.data.id)
            state.disciplines.data.splice(index, 1)
            state.disciplines.data.unshift(discipline.data)
        }
    },
    actions: {
        createDiscipline({commit}, disciplineData) {
            Methods.create(disciplineData, 'disciplines').then(discipline => {
                commit('ADD_DISCIPLINE', discipline)
            })
        },
        deleteDiscipline({commit}, discipline) {
            Methods.delete(discipline, 'disciplines').then(() => {
                commit('REMOVE_DISCIPLINE', discipline)
            })
        },
        getDisciplines({commit}) {
            Methods.list('disciplines').then(disciplines => {
                commit('SET_DISCIPLINES', {disciplines})
            })
        },
        updateDiscipline({commit}, discipline){
            Methods.update(discipline, 'disciplines').then(discipline => {
                commit('UPDATE_DISCIPLINE', discipline)
            })
        }
    },
}