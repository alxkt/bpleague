<template>
  <div class="header">
    <nav class="uk-navbar uk-navbar-container uk-navbar-transparent uk-padding-small"
         uk-navbar="dropbar: true; dropbar-mode: push">
      <div class="uk-navbar-left">
        <ul class="uk-navbar-nav uk-hidden@l">
          <li>
            <a class="uk-navbar-toggle" uk-navbar-toggle-icon></a>
            <div class="uk-navbar-dropdown" id="nav">
              <ul class="uk-nav uk-navbar-dropdown-nav">
                  <li class="uk-active"><a href="#">Classement</a></li>
                  <li><a href="#">Mes matchs</a></li>
              </ul>
              <hr class="uk-divider-icon">
              <a href="#" class="uk-button uk-button-text uk-width-1-1" v-if="name != null" v-on:click="logout">Connecté
                en tant que {{ name }}</a>
              <button class="uk-button uk-button-primary uk-width-1-1" href="#modal-full" uk-toggle>Ajouter un
                match
              </button>
            </div>
          </li>
        </ul>
        <a class="uk-navbar-item uk-logo uk-visible@l" href="#/main"><img src="../../assets/title.png"/></a>

        <ul class="uk-navbar-nav uk-visible@l">
          <li class="uk-active"><a href="#">Classement</a></li>
          <li><a href="#">Mes matchs</a></li>
        </ul>
      </div>

      <div class="uk-navbar-center uk-hidden@l">
        <a class="uk-navbar-item uk-logo" href="#/main"><img src="../../assets/title.png"/></a>
      </div>

      <div class="uk-navbar-right uk-visible@l">
        <a href="#" class="uk-button uk-button-text uk-margin-right" v-if="name != null" v-on:click="logout">Connecté en
          tant que {{ name }}</a>
        <button class="uk-button uk-button-primary uk-margin-right" href="#modal-full" uk-toggle>Ajouter un match
        </button>
      </div>
    </nav>

    <div class="uk-navbar-dropbar"></div>
  </div>
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
  .uk-logo img {
    max-height: 42px;
    margin-top: -4px;
  }

  #nav {
    width: 93%;
  }

  @media only screen and (max-width: 640px) {
    .uk-logo img {
      margin-top: 1px;
    }
  }
</style>
