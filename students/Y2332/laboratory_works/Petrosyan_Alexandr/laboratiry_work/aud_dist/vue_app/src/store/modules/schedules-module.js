import {Methods} from "../../api/methods";

export default {
    state: {
        schedules: [],
    },
    getters: {
        schedules: state => state.schedules,
    },
    mutations: {
        ADD_SCHEDULE(state, schedule) {
            state.schedules.data.unshift(schedule.data)
        },
        REMOVE_SCHEDULE(state, {id}) {
            let index = state.schedules.data.findIndex(schedule => schedule.id === id)
            state.schedules.data.splice(index, 1)
        },
        SET_SCHEDULES(state, {schedules}) {
            state.schedules = schedules
        },
        UPDATE_SCHEDULE(state, schedule) {
            let index = state.schedules.data.findIndex(s => s.id === schedule.data.id)
            state.schedules.data.splice(index, 1)
            state.schedules.data.unshift(schedule.data)
        }
    },
    actions: {
        createSchedule({commit}, scheduleData) {
            Methods.create(scheduleData, 'schedules').then(schedule => {
                commit('ADD_SCHEDULE', schedule)
            })
        },
        deleteSchedule({commit}, schedule) {
            Methods.delete(schedule, 'schedules').then(() => {
                commit('REMOVE_SCHEDULE', schedule)
            })
        },
        getSchedules({commit}) {
            Methods.list('schedules').then(schedules => {
                commit('SET_SCHEDULES', {schedules})
            })
        },
        updateSchedule({commit}, schedule){
            Methods.update(schedule, 'schedules').then(schedule => {
                commit('UPDATE_SCHEDULE', schedule)
            })
        }
    },
};