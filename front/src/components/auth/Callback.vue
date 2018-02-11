<template>
  <div class="callback">
    <img src="../../assets/title.png" id="title" class="uk-margin">
    <div class="uk-card uk-card-default uk-card-body uk-padding-large" id="loading">
      <div uk-spinner></div>
    </div>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Callback',
    mounted() {
      let login = this;

      const code = this.$route.query.code;
      const state = this.$route.query.state;
      auth.authorize(this, code, state);
    }
  }
</script>

<style scoped>
  .callback {
    width: 100%;
    text-align: center;
  }

  #title {
    width: 600px;
    max-width: 90%;
    margin-top: 3em;
  }

  #loading {
    width: 500px;
    max-width: 90%;
    margin: auto;
  }
</style>
