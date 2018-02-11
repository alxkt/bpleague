<template>
  <nav class="uk-navbar uk-navbar-container uk-navbar-transparent uk-padding-small uk-margin">
    <div class="uk-navbar-left">
      <a class="uk-navbar-item uk-logo" href="#/main"><img src="../../assets/title.png" id="logo"/></a>

      <ul class="uk-navbar-nav">
        <li class="uk-active"><a href="#">Classement</a></li>
        <li><a href="#">Mes matchs</a></li>
      </ul>
    </div>

    <div class="uk-navbar-right">
      <a href="#" class="uk-button uk-button-text uk-margin-right" v-if="name != null" v-on:click="logout">Connecté en tant que {{ name }}</a>
      <button class="uk-button uk-button-primary uk-margin-right" href="#modal-full" uk-toggle>Ajouter un match</button>
    </div>
  </nav>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Header',
    data() {
      return {
        name: null
      }
    },
    methods: {
      logout() {
        auth.logout();
      }
    },
    mounted() {
      let header = this;

      auth.checkAuth().then(() => {
        header.name = auth.user.profile.first_name;
      }).catch((err) => {
        console.log(err);
      });
    }
  }
</script>

<style scoped>
  #logo {
    max-height: 42px;
    margin-top: -4px;
  }
</style>
