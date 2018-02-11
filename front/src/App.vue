<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
  import UIkit from 'uikit';
  import Icons from 'uikit/dist/js/uikit-icons';

  // loads the Icon plugin
  UIkit.use(Icons);

  export default {
    name: 'App'
  }
</script>

<style lang="sass">
  @import "../node_modules/uikit/src/scss/variables-theme.scss"
  @import "../node_modules/uikit/src/scss/mixins-theme.scss"
  @import "../node_modules/uikit/src/scss/uikit-theme.scss"
</style>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
