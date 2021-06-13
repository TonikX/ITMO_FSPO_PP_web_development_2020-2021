import Vue from 'vue'
import Vuex from 'vuex'
import lecturers from "./modules/lecturers-module"
import disciplines from "./modules/disciplines-module"
import audiences from "./modules/audiences-module"
import groups from "./modules/groups-module"
import schedules from "./modules/schedules-module"

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        lecturers,
        disciplines,
        audiences,
        groups,
        schedules
    }
})
