import {Discipline} from "../../api/disciplines";

export default {
    state: {
        disciplines: []
    },
    getters: {
        disciplines: state => state.disciplines
    },
    mutations: {
        SET_DISCIPLINES(state, {disciplines}) {
            state.disciplines = disciplines
        }
    },
    actions: {
        getDisciplines({commit}) {
            Discipline.list().then(disciplines => {
                commit('SET_DISCIPLINES', {disciplines})
            })
        }
    },
}