<template>
  <div class="login">
    <img src="../assets/title.png" id="title" class="uk-margin">
    <div class="uk-card uk-card-default uk-card-body uk-padding-large" id="text">
      <h1 class="uk-heading-divider">Bienvenue</h1>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed elit convallis, laoreet nisl venenatis, placerat
      odio. Duis quis urna eu quam condimentum ullamcorper.<br/>

      <button class="uk-button uk-button-primary uk-margin uk-width-1-1" id="connect" v-on:click="login">Se connecter
      </button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    methods: {
      login() {

      }
    }
  }
</script>

<style scoped>
  .login {
    width: 100%;
    text-align: center;
  }

  #title {
    max-width: 600px;
    margin-top: 3em;
  }

  #text {
    max-width: 500px;
    margin: auto;
    text-align: left;
  }

  #connect {
  }
</style>
