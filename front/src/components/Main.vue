<template>
  <div class="main">
    <div class="uk-container">
      <h1 class="uk-heading-divider">Classement <span uk-icon="refresh" id="refresh" v-on:click="updateLeaderboard"></span></h1>

      <div class="uk-card uk-card-default uk-card-body uk-padding-large uk-overflow-auto" id="leaderboard">
        <nav class="uk-navbar-container" uk-navbar>
          <div class="uk-navbar-left">
            <div class="uk-navbar-item">
              <form class="uk-search uk-search-navbar">
                <span uk-search-icon></span>
                <input class="uk-search-input" type="search" placeholder="Search..." v-model="search">
              </form>
            </div>
          </div>
        </nav>
        <table class="uk-table uk-table-divider uk-table-hover" v-if="users.length > 0">
          <thead>
          <tr>
            <th class="uk-table-shrink">#</th>
            <th class="uk-width-large">Nom</th>
            <th class="uk-width-small uk-visible@s">Points</th>
            <th class="uk-width-small uk-hidden@s">Pts</th>
            <th class="uk-width-small uk-visible@s">Joués</th>
            <th class="uk-width-small uk-hidden@s">J</th>
            <th class="uk-width-small uk-visible@s">Victoires</th>
            <th class="uk-width-small uk-hidden@s">V</th>
            <th class="uk-width-small uk-visible@s">Defaites</th>
            <th class="uk-width-small uk-hidden@s">D</th>
            <th class="uk-width-small uk-visible@s">Goal Average</th>
            <th class="uk-width-small uk-hidden@s">GA</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="user in users_filtered" v-if="user.score > 0" v-bind:class="{ me: user.id === me_id }">
            <td>{{ users.indexOf(user) + 1 }}</td>
            <td>{{ user.first_name }} {{ user.last_name }}</td>
            <td>{{ user.score }}</td>
            <td>{{ user.matches }}</td>
            <td>{{ user.victories }}</td>
            <td>{{ user.looses }}</td>
            <td>{{ user.goal_average }}</td>
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
        users_filtered: [],
        me_id: auth.user.profile.id,
        search: ''
      }
    },
    watch: {
      search: function (newSearch, oldSearch) {
        this.updateFiltering();
      }
    },
    components: {
      AddMatch
    },
    mounted() {
      this.updateLeaderboard();

      this.$root.$on('updateLeaderboard', () => {
          this.updateLeaderboard();
      })
    },
    methods: {
      updateLeaderboard() {
        let main = this;

        this.users = [];
        axios.get(process.env.API_URL + '/users?score=true')
          .then(function (response) {
            main.users = response.data;
            main.updateFiltering();
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      updateFiltering() {
        this.users_filtered = this.users.reduce((users, user) => {
          if (user.first_name.toLocaleLowerCase().includes(this.search.toLocaleLowerCase()) || user.last_name.toLocaleLowerCase().includes(this.search.toLocaleLowerCase())) {
            users.push(user);
          }
          return users;
        }, []);
      }
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

  #refresh {
    margin-top: 0.5em;
    float: right;
  }

  #refresh:hover {
    -webkit-animation: rotating 1s linear infinite;
    -moz-animation: rotating 1s linear infinite;
    -ms-animation: rotating 1s linear infinite;
    -o-animation: rotating 1s linear infinite;
    animation: rotating 1s linear infinite;
  }

  @-webkit-keyframes rotating /* Safari and Chrome */
  {
    from {
      -webkit-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    to {
      -webkit-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }

  @keyframes rotating {
    from {
      -ms-transform: rotate(0deg);
      -moz-transform: rotate(0deg);
      -webkit-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    to {
      -ms-transform: rotate(360deg);
      -moz-transform: rotate(360deg);
      -webkit-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }

</style>
