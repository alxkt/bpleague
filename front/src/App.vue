<template>
  <div id="app" class="uk-background-default">
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style lang="sass">
  $global-background: rgb(254, 254, 254)
  $global-color: rgb(54, 56, 69)
  $global-inverse-color: rgb(254, 254, 254)
  $global-primary-background: rgb(134, 141, 245)
  $global-secondary-background: rgb(54, 56, 69)
  $global-danger-background: rgb(227, 160, 164)

  @import "../node_modules/uikit/src/scss/variables-theme.scss"
  @import "../node_modules/uikit/src/scss/mixins-theme.scss"
  @import "../node_modules/uikit/src/scss/uikit-theme.scss"
</style>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
</style>
