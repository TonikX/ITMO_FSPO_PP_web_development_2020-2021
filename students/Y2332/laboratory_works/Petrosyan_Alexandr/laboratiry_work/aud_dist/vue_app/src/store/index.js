import Vue from 'vue'
import Vuex from 'vuex'
import lecturers from "./modules/lecturers-module"
import disciplines from "./modules/disciplines-module"

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        lecturers,
        disciplines
    }
})
