<template>
  <div id="app">
    <div class="container">
      <div class="columns is-mobile">
        <transition name="fade" mode="out-in">
          <component class="lock-height column is-9 component-bg" :updateView.sync="current_view" :is="current_view"></component>
        </transition>
        <ToolsBar class="column is-3 component-bg" :updateView.sync="current_view"></ToolsBar>
      </div>
    </div>
  </div>
</template>

<script>
import ToolsBar from '@/components/toolsBar'
import AccountList from '@/components/accountList'
import Editer from '@/components/editor'
import Details from '@/components/details'

export default {
  name: 'app',
  data() {
    return {
      current_view: 'account-list',
      current_oper: ''
    }
  },
  components: {
    ToolsBar,
    'account-list': AccountList,
    'editor': Editer,
    'account-details': Details
  }
}
</script>

<style lang="less">
@import 'assets/bulma-0.5.0/css/bulma.css';
@import url('assets/icon.less');

#app {
  background-color: hsl(217, 71%, 53%);

  .component-bg {
    background-color: #FFF;
  }

  .columns, .column {
    margin: 0;
  }

  .fade-list-enter-active, .fade-list-leave-active {
    transition: opacity .5s, height .5s;
  }
  .fade-list-enter, .fade-list-leave-to {
    opacity: 0;
    height: 0;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity .25s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  .lock-height {
    height: 100vh;
    overflow: auto;
  }
}
</style>
