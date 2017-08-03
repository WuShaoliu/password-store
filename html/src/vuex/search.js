const search = {
    state: {
        keyword: '',
        key: {
            all: '全部',
            website: '站点',
            username: '用户名',
            email: '邮箱',
            phone: '手机',
        },
        activeKey: 'all'
    },
    mutations: {
        SET_SEARCH_KEYWORD(state, key) {
            state.activeKey = key
        },
        SET_KEYWORD(state, keyword) {
            state.keyword = keyword
        }
    },
    actions: {
        setSearchKey({commit}, key) {
            commit('SET_SEARCH_KEYWORD', key)
        },
        setKeyword({commit}, keyword) {
            commit('SET_KEYWORD', keyword)
        }
    },
    getters: {
        searchKeyword: state => state.keyword,
        searchKey: state => state.key,
        searchActiveKey: state => state.activeKey
    }
}

export default search