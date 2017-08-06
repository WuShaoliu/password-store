<template>
<div id="tools-bar">
  <aside class="menu">
    <p class="menu-label">
      控制项
    </p>
    <transition name="fade" mode="out-in">
    <ul class="menu-list" v-if="updateView=='editor' || updateView=='account-details'" key="editor">
      <li><a class="iconfont icon-add" href="javascript:;" @click="show_list()"> 查看列表</a></li>
    </ul>
    <!--<ul class="menu-list" v-if="updateView=='account-list'">-->
    <ul class="menu-list" v-if="updateView=='account-list'" key="account-list">
      <li>
        <div class="field has-addons">
          <p class="control">
            <span class="select">
              <select v-model="search_key">
                <option :value="key" v-for="item, key in searchKey">{{ item }}</option>
              </select>
            </span>
          </p>
          <p class="control"><input class="input" placeholder="Search" :value="searchKeyword" @keydown.13="set_keyword" @blur="set_keyword"></p>
        </div>
      </li>
      <li><a class="iconfont icon-delete" href="javascript:;" @click="show_details()"> 查看</a></li>
      <li><a class="iconfont icon-add" href="javascript:;" @click="add_account()"> 添加</a></li>
      <li><a class="iconfont icon-edit" href="javascript:;" @click="edit_account()"> 编辑</a></li>
      <li><a class="iconfont icon-delete" href="javascript:;" @click="deleteAccount()"> 删除</a></li>
    </ul>
    </transition>
  </aside>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  computed: {
    ...mapGetters([
      'activeAccount',
      'searchKey',
      'searchKeyword',
      'searchActiveKey'
    ]),
    search_key: {
      get () {
        return this.searchActiveKey
      },
      set (value) {
        this.setSearchKey(value)
      }
    }
  },
  props: [
    'updateView'
  ],
  methods: {
    ...mapActions([
      'setActiveAccount',
      'deleteAccount',
      'setKeyword',
      'setSearchKey'
    ]),
    add_account() {
      this.setActiveAccount({website: '', username: '', password: '', email: '', phone: '', asks: [], remarks: ''}),
      this.$emit('update:updateView', 'editor')
    },
    edit_account() {
      if (JSON.stringify(this.activeAccount) == '{}') {
        alert('请选择对象')
        return
      }
      this.$emit('update:updateView', 'editor')
    },
    show_details() {
      if (JSON.stringify(this.activeAccount) == '{}') {
        alert('请选择对象')
        return
      }
      this.$emit('update:updateView', 'account-details')
    },
    show_list() {
      this.$emit('update:updateView', 'account-list')
    },
    set_keyword(e) {
      this.setKeyword(e.target.value)
    }
  }
}
</script>

<style lang="less">
</style>