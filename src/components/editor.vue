<template>
<div id="editor">
  <div class="field is-horizontal">
    <div class="field-body">
      <div class="field">
        <label for="username" class="label">用户名</label>
        <div class="control">
          <input id="username" type="text" class="input" placeholder="Username" v-model="account.username">
        </div>
      </div>
      <div class="field">
        <label for="account" class="label">密码</label>
        <div class="control">
          <input id="account" type="text" class="input" placeholder="Password" v-model="account.password">
        </div>
      </div>
    </div>
  </div>
  <div class="field is-horizontal">
    <div class="field-body">
      <div class="field">
        <label for="website" class="label">登录站点</label>
        <div class="control">
          <input id="website" type="text" class="input" placeholder="Website" v-model="account.website">
        </div>
      </div>
      <div class="field">
        <label for="email" class="label">电子邮箱</label>
        <div class="control">
          <input id="email" type="text" class="input" placeholder="Email" v-model="account.email">
        </div>
      </div>
    </div>
  </div>
  <div class="field is-horizontal">
    <div class="field-body">
      <div class="field">
        <label for="phone" class="label">手机号码</label>
        <div class="control">
          <input id="phone" type="text" class="input" placeholder="Phone" v-model="account.phone">
        </div>
      </div>
      <div class="field">
        <label for="remarks" class="label">备注</label>
        <div class="control">
          <input id="remarks" type="text" class="input" placeholder="Remarks" v-model="account.remarks">
        </div>
      </div>
    </div>
  </div>
  <nav class="breadcrumb">
    <ul>
      <li :class="{'is-active': active_ask_index==index}" v-for="ask, index in account.asks">
        <a href="javascript:;" @click="active_ask_index = index">问题{{ index }}</a>
        <a class="iconfont icon-delete active-event" href="javascript:;" @click="delete_ask(index)"></a>
      </li>
    </ul>
  </nav>
  <transition name="fade">
    <hr v-if="active_ask_index >= 0" key="active-ask">
  </transition>
  <transition name="fade">
    <div class="field is-horizontal" v-if="active_ask_index >= 0" key="active-ask-hr">
      <div class="field-body">
        <div class="field">
          <label for="website" class="label">提问</label>
          <div class="control">
            <input ref="ask" id="website" type="text" class="input" placeholder="Website"
            v-model="account.asks[active_ask_index].ask">
          </div>
        </div>
        <div class="field">
          <label for="website" class="label">答案</label>
          <div class="control">
            <input id="website" type="text" class="input" placeholder="Website"
            v-model="account.asks[active_ask_index].answer">
          </div>
        </div>
      </div>
    </div>
  </transition>
  <hr>
  <div class="field is-grouped is-grouped-right">
    <div class="control">
      <button class="button" @click="add_ask()">添加密保问题</button>
      <button class="button is-primary" @click="submit()">提交</button>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'editor',
  data() {
    return {
      active_ask_index: -1,
      account: {}
    }
  },
  computed: {
    ...mapGetters([
      'activeAccount'
    ])
  },
  mounted() {
    this.account = this.activeAccount
    if (this.account.asks.length > 0) {
      this.active_ask_index = 0
    }
  },
  methods: {
    ...mapActions([
      'addAccount',
      'editAccount',
      'setActiveAccount'
    ]),
    add_ask() {
      let ask = {
        ask: '',
        answer: ''
      }
      this.account.asks.push(ask)
      this.active_ask_index = this.account.asks.length - 1
      
      this.$nextTick(() => {
          this.$refs.ask.focus()
      })
    },
    delete_ask(index) {
      this.account.asks.splice(index, 1)
      this.active_ask_index -= 1
    },
    async submit() {
      if (this.account.id) {
        this.editAccount(this.account)
        this.setActiveAccount({})
      }
      else {
        this.addAccount(this.account)
      }
    }
  }
}
</script>

<style lang="less">
  #editor {
    .breadcrumb li.is-active a.active-event {
      pointer-events: auto;
    }
  }
</style>