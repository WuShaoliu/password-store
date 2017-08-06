import Vuex from 'vuex'
import Vue from 'vue'

import account from './account'
import search from './search'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        account,
        search
    }
})
