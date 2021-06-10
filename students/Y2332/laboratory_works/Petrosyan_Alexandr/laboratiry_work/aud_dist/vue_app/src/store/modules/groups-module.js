import {Methods} from "../../api/methods";

export default {
    state: {
        groups: [],
    },
    getters: {
        groups: state => state.groups,
    },
    mutations: {
        ADD_GROUP(state, group) {
            state.groups.data.unshift(group.data)
        },
        REMOVE_GROUP(state, {id}) {
            let index = state.groups.data.findIndex(group => group.id === id)
            state.groups.data.splice(index, 1)
        },
        SET_GROUPS(state, {groups}) {
            state.groups = groups
        },
        UPDATE_GROUP(state, group) {
            let index = state.groups.data.findIndex(g => g.id === group.data.id)
            state.groups.data.splice(index, 1)
            state.groups.data.unshift(group.data)
        }
    },
    actions: {
        createGroup({commit}, groupData) {
            Methods.create(groupData, 'groups').then(group => {
                commit('ADD_GROUP', group)
            })
        },
        deleteGroup({commit}, group) {
            Methods.delete(group, 'groups').then(() => {
                commit('REMOVE_GROUP', group)
            })
        },
        getGroups({commit}) {
            Methods.list('groups').then(groups => {
                commit('SET_GROUPS', {groups})
            })
        },
        updateGroup({commit}, group){
            Methods.update(group, 'groups').then(group => {
                commit('UPDATE_GROUP', group)
            })
        }
    },
};