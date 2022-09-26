import {Methods} from "../../api/methods";


export default {
    state: {
        audiences: []
    },
    getters: {
        audiences: state => state.audiences
    },
    mutations: {
        ADD_AUDIENCE(state, audience) {
            state.audiences.data.unshift(audience.data)
        },
        REMOVE_AUDIENCE(state, {id}) {
            let index = state.audiences.data.findIndex(audience => audience.id === id)
            state.audiences.data.splice(index, 1)
        },
        SET_AUDIENCES(state, {audiences}) {
            state.audiences = audiences
        },
        UPDATE_AUDIENCE(state, audience) {
            let index = state.audiences.data.findIndex(d => d.id === audience.data.id)
            state.audiences.data.splice(index, 1)
            state.audiences.data.unshift(audience.data)
        }
    },
    actions: {
        createAudience({commit}, audiencesData) {
            Methods.create(audiencesData, 'audiences').then(audience => {
                commit('ADD_AUDIENCE', audience)
            })
        },
        deleteAudience({commit}, audience) {
            Methods.delete(audience, 'audiences').then(() => {
                commit('REMOVE_AUDIENCE', audience)
            })
        },
        getAudiences({commit}) {
            Methods.list('audiences').then(audiences => {
                commit('SET_AUDIENCES', {audiences})
            })
        },
        updateAudience({commit}, audience){
            Methods.update(audience,'audiences').then(audience => {
                commit('UPDATE_AUDIENCE', audience)
            })
        }
    },
}