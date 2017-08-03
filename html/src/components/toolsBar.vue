<template>
<div id="tools-bar">
  <aside class="menu">
    <p class="menu-label">
      控制项
    </p>
    <transition name="fade" mode="out-in">
    <ul class="menu-list" v-if="updateView=='editor'" key="editor">
      <li><a class="iconfont icon-add" href="javascript:;" @click="show_list()"> 查看列表</a></li>
    </ul>
    <!--<ul class="menu-list" v-if="updateView=='password-list'">-->
    <ul class="menu-list" v-if="updateView=='password-list'" key="password-list">
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
      <li><a class="iconfont icon-add" href="javascript:;" @click="add_password()"> 添加</a></li>
      <li><a class="iconfont icon-edit" href="javascript:;" @click="edit_password()"> 编辑</a></li>
      <li><a class="iconfont icon-delete" href="javascript:;" @click="deletePassword()"> 删除</a></li>
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
      'activePassword',
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
      'setActivePassword',
      'deletePassword',
      'setKeyword',
      'setSearchKey'
    ]),
    add_password() {
      this.setActivePassword({website: '', username: '', password: '', email: '', phone: '', asks: []}),
      this.$emit('update:updateView', 'editor')
    },
    edit_password() {
      if (JSON.stringify(this.activePassword) == '{}') {
        alert('请选择对象')
        return
      }
      this.$emit('update:updateView', 'editor')
    },
    show_list() {
      this.setActivePassword({}),
      this.$emit('update:updateView', 'password-list')
    },
    set_keyword(e) {
      this.setKeyword(e.target.value)
    }
  }
}
</script>

<style lang="less">
</style>