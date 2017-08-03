<template>
  <div id="password-list">
    <table class="table is-striped is-fullwidth">
      <thead>
        <tr>
          <th>注册站点</th>
          <th>用户名</th>
          <th>密码</th>
          <th>电子邮箱</th>
          <th>手机号码</th>
          <th>更新时间</th>
        </tr>
      </thead>
      <transition-group name="fade-list" tag="tbody">
        <tr :class="{'is-selected': activePassword == password}" v-for="password in sort"
        @click="setActivePassword(password)" :key="password.id">
          <td>{{ password.website }}</td>
          <td>{{ password.username }}</td>
          <td>{{ password.password }}</td>
          <td>{{ password.email }}</td>
          <td>{{ password.phone }}</td>
          <td>{{ new Date(password.edit_time * 1000).toLocaleString() }}</td>
        </tr>
      </transition-group>
    </table>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'password-list',
  mounted() {
    this.getPasswordList()
  },
  computed: {
    ...mapGetters([
      'activePassword',
      'passwordList',
      'searchActiveKey',
      'searchKeyword'
    ]),
    sort () {
      return this.passwordList.filter(this.search)
    }
  },
  methods: {
    ...mapActions([
      'getPasswordList',
      'setActivePassword'
    ]),
    search(obj) {
      let keyword = this.searchKeyword.toLowerCase()
      let website = obj.website.toLowerCase()
      let username = obj.website.toLowerCase()
      let email = obj.website.toLowerCase()
      let phone = obj.website.toLowerCase()
      if (this.searchActiveKey == 'all') {
        return obj.website.indexOf(keyword) != -1 || obj.username.indexOf(keyword) != -1 ||
        obj.email.indexOf(keyword) != -1 || obj.phone.indexOf(keyword) != -1
      }
      else if (this.searchActiveKey == 'website') {
        return obj.website.indexOf(keyword) != -1
      }
      else if (this.searchActiveKey == 'username') {
        return obj.username.indexOf(keyword) != -1
      }
      else if (this.searchActiveKey == 'email') {
        return  obj.email.indexOf(keyword) != -1
      }
      else if (this.searchActiveKey == 'phone') {
        return obj.phone.indexOf(keyword) != -1
      }
      else {
        return true
      }
    }
  }
}
</script>