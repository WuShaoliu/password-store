import Vuex from 'vuex'
import Vue from 'vue'

import password from './password'
import search from './search'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        password,
        search
    }
})
