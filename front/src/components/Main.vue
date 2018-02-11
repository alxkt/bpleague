<template>
  <div class="main">
    <div class="uk-container">
      <h1 class="uk-heading-divider">Classement</h1>

      <div class="uk-card uk-card-default uk-card-body uk-padding-large uk-overflow-auto" id="leaderboard">
        <nav class="uk-navbar-container" uk-navbar>
          <div class="uk-navbar-left">
            <div class="uk-navbar-item">
              <form class="uk-search uk-search-navbar">
                <span uk-search-icon></span>
                <input class="uk-search-input" type="search" placeholder="Search...">
              </form>
            </div>
          </div>
        </nav>
        <table class="uk-table uk-table-divider uk-table-hover" v-if="users.length > 0">
          <thead>
          <tr>
            <th class="uk-table-shrink">Position</th>
            <th class="uk-width-large">Nom</th>
            <th class="uk-width-small">V / D</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="user in users" v-if="user.score > 0" v-bind:class="{ me: user.id === me_id }">
            <td>{{ users.indexOf(user) + 1 }}</td>
            <td>{{ user.first_name }} {{ user.last_name }}</td>
            <td>{{ user.score }}</td>
          </tr>
          </tbody>
        </table>
        <div uk-spinner v-else id="spinner"></div>
      </div>
    </div>

    <add-match></add-match>
  </div>
</template>

<script>
  import AddMatch from './AddMatch';
  import auth from '../modules/auth';
  import axios from 'axios';

  export default {
    name: 'Main',
    data() {
      return {
        users: [],
        me_id: auth.user.profile.id
      }
    },
    components: {
      AddMatch
    },
    mounted() {
      let main = this;

      axios.get(process.env.API_URL + '/users?score=true')
        .then(function (response) {
          main.users = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }
</script>

<style scoped>
  .main {
    width: 100%;
  }

  .uk-card {
    margin: 3em auto auto;
  }

  #spinner {
    margin-left: 45%;
    margin-top: 5em;
  }

  .me {
    background-color: rgba(216, 245, 221, 0.69);
  }

</style>
