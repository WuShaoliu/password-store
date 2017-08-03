import api from '@/fetch'

const password = {
    state: {
        passwordList: [],
        activePassword: {}
    },
    mutations: {
        async GET_PASSWORD_LIST(state) {
            let resp = await api.get_passwords()
            state.passwordList = resp.data
        },
        SET_ACTIVE_PASSWORD(state, password) {
            if (state.activePassword == password) {
                state.activePassword = {}
            }
            else {
                state.activePassword = password
            }
        },
        async ADD_PASSWORD(state, password) {
            let resp = await api.add_passwords(password)
            alert(resp.msg)
        },
        async EDIT_PASSWORD(state) {
            let resp = await api.edit_passwords(state.activePassword)
            alert(resp.msg)
        },
        async DELETE_PASSWORD(state) {
            if (JSON.stringify(state.activePassword) == '{}') {
                alert('请选择对象')
                return
            }
            else {
                let resp = api.delete_password(state.activePassword)
                alert(resp.msg)
            }
        }
    },
    actions: {
        getPasswordList({commit}) {
            commit('GET_PASSWORD_LIST')
        },
        setActivePassword({commit}, password) {
            commit('SET_ACTIVE_PASSWORD', password)
        },
        addPassword({commit}, password) {
            commit('ADD_PASSWORD', password)
        },
        editPassword({commit}, password) {
            commit('EDIT_PASSWORD', password)
            commit('GET_PASSWORD_LIST')
        },
        deletePassword({commit}) {
            commit('DELETE_PASSWORD')
            commit('GET_PASSWORD_LIST')
        }
    },
    getters: {
        passwordList: state => state.passwordList,
        activePassword: state => state.activePassword,
    }
}

export default password