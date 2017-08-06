import api from '@/fetch'

const account = {
    state: {
        accountList: [],
        activeAccount: {}
    },
    mutations: {
        async GET_PASSWORD_LIST(state) {
            let resp = await api.get_accounts()
            state.accountList = resp.data
        },
        SET_ACTIVE_PASSWORD(state, account) {
            if (state.activeAccount == account) {
                state.activeAccount = {}
            }
            else {
                state.activeAccount = account
            }
        },
        async ADD_PASSWORD(state, account) {
            let resp = await api.add_accounts(account)
            alert(resp.msg)
        },
        async EDIT_PASSWORD(state) {
            let resp = await api.edit_accounts(state.activeAccount)
            alert(resp.msg)
        },
        async DELETE_PASSWORD(state) {
            if (JSON.stringify(state.activeAccount) == '{}') {
                alert('请选择对象')
                return
            }
            else {
                let resp = await api.delete_account(state.activeAccount)
                alert(resp.msg)
            }
        }
    },
    actions: {
        getAccountList({commit}) {
            commit('GET_PASSWORD_LIST')
            commit('SET_ACTIVE_PASSWORD', {})
        },
        setActiveAccount({commit}, account) {
            commit('SET_ACTIVE_PASSWORD', account)
        },
        addAccount({commit}, account) {
            commit('ADD_PASSWORD', account)
        },
        editAccount({commit}, account) {
            commit('EDIT_PASSWORD', account)
            commit('GET_PASSWORD_LIST')
        },
        deleteAccount({commit}) {
            commit('DELETE_PASSWORD')
            commit('GET_PASSWORD_LIST')
        }
    },
    getters: {
        accountList: state => state.accountList,
        activeAccount: state => state.activeAccount,
    }
}

export default account