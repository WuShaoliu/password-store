<template>
<div id="details">
  <div class="tile is-ancestor">
    <div class="tile is-parent is-vertical">
      <article class="tile is-child notification is-success">
        <h4>注册站点</h4>
        <p>{{ activeAccount.website }}</p>
        <h4>用户名</h4>
        <p>{{ activeAccount.username }}</p>
        <h4>密码</h4>
        <p>{{ activeAccount.password }}</p>
      </article>
    </div>
    <div class="tile is-parent is-vertical"
    v-if="activeAccount.email || activeAccount.phone || activeAccount.remarks">
      <article class="tile is-child notification is-info">
        <h4 v-if="activeAccount.email">电子邮箱</h4>
        <p v-if="activeAccount.email">{{ activeAccount.email }}</p>
        <h4 v-if="activeAccount.phone">手机号码</h4>
        <p v-if="activeAccount.phone">{{ activeAccount.phone }}</p>
        <h4 v-if="activeAccount.remarks">备注</h4>
        <p v-if="activeAccount.remarks">{{ activeAccount.remarks }}</p>
      </article>
    </div>
  </div>

  <div class="tile is-ancestor" v-if="activeAccount.asks.length > 0">
    <div class="tile is-parent" v-for="ask in activeAccount.asks">
      <article class="tile is-child notification is-light">
        <h4>提问</h4>
        <p>{{ ask.ask }}</p>
        <h4>答案</h4>
        <p>{{ ask.answer }}</p>
      </article>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'account-details',
  computed: {
    ...mapGetters([
      'activeAccount',
    ]),
  }
}
</script>