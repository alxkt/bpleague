<template>
  <div class="login">
    <img src="../../assets/title.png" id="title" class="uk-margin">
    <div class="uk-card uk-card-default uk-card-body uk-padding-large" id="text">
      <h1 class="uk-heading-divider">Bienvenue</h1>
      <p>
        <b>BPLeague</b> est le site de League de Bière-Pong de CentraleSupéléc, developpé en collaboration avec
        l'<b>AdR</b>.<br/>
      </p>
      <button class="uk-button uk-button-primary uk-margin uk-width-1-1" id="connect" v-on:click="login">Se connecter
      </button>
      <h3 class="uk-heading-divider">Concept</h3>
      <p>
        Rentrez chaque match que vous disputez en indiquant votre partenaire et vos adversaires ainsi que le score final.
        Suivant ce score, un nombre de point est attribué à chaque équipe et un classement est determiné en temps réel.
        En cas de litige, un mail est envoyé aux adversaires qui pourront contester le match.
      </p>
    </div>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Login',
    mounted() {
      let login = this;

      auth.checkAuth().then(() => {
        login.$router.replace('/main');
      }).catch(() => {
      });
    },
    methods: {
      login() {
        auth.login(this);
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
    width: 600px;
    max-width: 90%;
    margin-top: 3em;
  }

  #text {
    width: 500px;
    max-width: 90%;
    margin: auto;
    text-align: left;
  }
</style>
