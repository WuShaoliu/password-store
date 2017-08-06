<template>
  <div id="account-list">
    <table class="table is-striped is-fullwidth">
      <thead>
        <tr>
          <th>#</th>
          <th>注册站点</th>
          <th>用户名</th>
          <th>密码</th>
          <th>电子邮箱</th>
          <th>手机号码</th>
          <!--<th>更新时间</th>-->
        </tr>
      </thead>
      <transition-group name="fade-list" tag="tbody">
        <tr :class="{'is-selected': activeAccount == account}" v-for="account, index in sort"
        @click="setActiveAccount(account)" :key="account.id">
          <td>{{ index }}</td>
          <td>{{ account.website }}</td>
          <td>{{ account.username }}</td>
          <td>{{ account.password }}</td>
          <td>{{ account.email }}</td>
          <td>{{ account.phone }}</td>
          <!--<td>{{ new Date(account.edit_time * 1000).toLocaleString() }}</td>-->
        </tr>
      </transition-group>
    </table>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'account-list',
  mounted() {
    this.getAccountList()
  },
  computed: {
    ...mapGetters([
      'activeAccount',
      'accountList',
      'searchActiveKey',
      'searchKeyword'
    ]),
    sort () {
      return this.accountList.filter(this.search)
    }
  },
  methods: {
    ...mapActions([
      'getAccountList',
      'setActiveAccount'
    ]),
    search(obj) {
      let keyword = this.searchKeyword.toLowerCase()
      let website = obj.website.toLowerCase()
      let username = obj.username.toLowerCase()
      let email = obj.email.toLowerCase()
      let phone = obj.phone.toLowerCase()
      let remarks = obj.remarks.toLowerCase()
      if (this.searchActiveKey == 'all') {
        return obj.website.indexOf(keyword) != -1 || obj.username.indexOf(keyword) != -1 ||
        obj.email.indexOf(keyword) != -1 || obj.phone.indexOf(keyword) != -1 || obj.remarks.indexOf(keyword) != -1
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
      else if (this.searchActiveKey == 'remarks') {
        return obj.remarks.indexOf(keyword) != -1
      }
      else {
        return true
      }
    }
  }
}
</script>