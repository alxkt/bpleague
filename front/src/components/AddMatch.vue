<template>
  <div class="add-match">
    <v-card flat>
      <v-layout row pb-2>
        <v-flex xs12 md8 offset-md2>
          <v-stepper v-model="step">
            <v-stepper-header>
              <v-stepper-step step="1" :complete="step > 1">Votre équipe</v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step step="2">Vos adversaires</v-stepper-step>
            </v-stepper-header>
            <v-stepper-items>
              <v-stepper-content step="1">
                <div style="padding: 1em;" v-if="step == 1">
                  <span class="headline">Votre équipe</span>
                  <v-divider style="margin-bottom: 1em;"></v-divider>
                  <v-menu full-width :open-on-click="false" :close-on-click="false" :value="search.length > 0" offset-y>
                  <v-text-field
                    slot="activator"
                    v-model="ally.name"
                    label="Votre partenaire"
                    id="testing"
                    autofocus
                    clearable
                    :loading="loading"
                  ></v-text-field>
                  <v-progress-linear
                    slot="progress"
                    height="7"
                    color="primary"
                  ></v-progress-linear>
                  <v-list>
                    <v-list-tile v-for="ally_search in search" :key="ally_search.id" @click="select(ally, ally_search)" class="search">
                      <v-list-tile-title>{{ ally_search.name }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>
                  <v-slider v-model="score_us" thumb-label step="1" max="10" ticks label="Vos verres restants"></v-slider>
                </div>
                <v-btn color="primary" @click.native="step = 2">Next !</v-btn>
                <v-btn flat to="/main">Cancel</v-btn>
              </v-stepper-content>
              <v-stepper-content step="2">
                <div style="padding: 1em;" v-if="step == 2">
                  <span class="headline">Vos adversaires</span>
                  <v-divider style="margin-bottom: 1em;"></v-divider>
                  <v-menu full-width :open-on-click="false" :close-on-click="false" :value="search.length > 0 && adversaryA.id === null" offset-y>
                  <v-text-field
                    slot="activator"
                    v-model="adversaryA.name"
                    label="Adversaire 1"
                    id="testing"
                    :loading="loading"
                  ></v-text-field>
                  <v-progress-linear
                    slot="progress"
                    height="7"
                    color="primary"
                  ></v-progress-linear>
                  <v-list>
                    <v-list-tile v-for="adversary_search in search" :key="adversary_search.id" @click="select(adversaryA, adversary_search)" class="search">
                      <v-list-tile-title>{{ adversary_search.name }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>
                  <v-menu full-width :open-on-click="false" :close-on-click="false" :value="search.length > 0 && adversaryA.id !== null" offset-y>
                  <v-text-field
                    slot="activator"
                    v-model="adversaryB.name"
                    label="Adversaire 2"
                    id="testing"
                    :loading="loading"
                  ></v-text-field>
                  <v-progress-linear
                    slot="progress"
                    height="7"
                    color="primary"
                  ></v-progress-linear>
                  <v-list>
                    <v-list-tile v-for="adversary_search in search" :key="adversary_search.id" @click="select(adversaryB, adversary_search)" class="search">
                      <v-list-tile-title>{{ adversary_search.name }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>
                  <v-slider v-model="score_them" thumb-label step="1" max="10" ticks label="Leurs verres restants"></v-slider>
                </div>
                <v-btn color="primary" @click="addMatch()">Add match !</v-btn>
                <v-btn flat @click="step = 1">Cancel</v-btn>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-flex>
      </v-layout>
    </v-card>

    <v-snackbar top v-model="snackbar">
      {{ snackbar_text }}
      <v-btn flat color="pink" @click.native="snackbar = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
  import axios from 'axios';
  import _ from 'lodash';

  import matchs from '../modules/matchs';
  import auth from '../modules/auth';

  function init() {
    return {
      loading: false,
      snackbar: false,
      snackbar_text: '',
      score_us: 0,
      score_them: 0,
      step: 0,
      ally: {
        name: '',
        id: null
      },
      adversaryA: {
        name: '',
        id: null
      },
      adversaryB: {
        name: '',
        id: null
      },
      search: [],
      searchNames: []
    }
  }

  export default {
    name: 'AddMatch',
    data() {
      return init();
    },
    computed: {
      ally_name() {
        return this.ally.name;
      },
      adversaryA_name() {
        return this.adversaryA.name;
      },
      adversaryB_name() {
        return this.adversaryB.name;
      }
    },
    watch: {
      ally_name: function (newAlly) {
        if (!this.searchNames.includes(newAlly)) {
          this.ally.id = null;
        }
        this.getUsers(newAlly);
      },
      adversaryA_name: function (newAdversary) {
        if (!this.searchNames.includes(newAdversary)) {
          this.adversaryA.id = null;
        }
        this.getUsers(newAdversary);
      },
      adversaryB_name: function (newAdversary) {
        if (!this.searchNames.includes(newAdversary)) {
          this.adversaryB.id = null;
        }
        this.getUsers(newAdversary);
      }
    },
    methods: {
      getUsers: _.debounce(
        function (search) {
          let addMatch = this;
          const me_id = auth.user.profile.id;
          this.loading = true;
          axios.get(process.env.API_URL + '/users?search=' + search + '&max=10')
            .then(function (response) {
              addMatch.search = response.data;
              addMatch.search = addMatch.search.reduce(function (a, b) {
                let people = b;
                people.name = people.first_name + ' ' + people.last_name;
                addMatch.searchNames.push(people.name);
                if (people.id !== addMatch.ally.id && people.id !== addMatch.adversaryA.id && people.id !== addMatch.adversaryB.id && people.id !== me_id) {
                  a.push(people);
                }
                return a;
              }, []);
              addMatch.loading = false;
            })
            .catch(function (error) {
              console.log(error);
            });
        },
        500
      ),
      select: function (field, search) {
        field.name = search.name;
        field.id = search.id;
      },
      addMatch: function () {
        const me_id = auth.user.profile.id;
        let vw = this;
        if (this.ally.id == null) {
          this.snackbar_text = 'Vous n\'avez pas mis de partenaire !';
          this.snackbar = true;
        } else if (this.adversaryA.id == null || this.adversaryB.id == null) {
          this.snackbar_text = 'Vous n\'avez pas mis d\'adversaire !';
          this.snackbar = true;
        } else if ((this.score_us !== 0 && this.score_them !== 0) || (this.score_us === 0 && this.score_them === 0)) {
          this.snackbar_text = 'Vous n\'avez pas mis de score cohérent !';
          this.snackbar = true;
        } else {
          matchs.addMatch(me_id, this.ally.id, this.adversaryA.id, this.adversaryB.id, this.score_us, this.score_them).then(() => {
            this.snackbar_text = 'Match ajouté avec succés.';
            this.snackbar = true;
            Object.assign(this.$data, init());
            vw.$root.$emit('updateLeaderboard', true);
          }).catch(() => {
          });
        }
      }
    }
  }
</script>

<style scoped>
  .add-match {
    margin-top: 2em;
  }

  #splash {
    background-image: url('../assets/images/splash.jpg');
  }

</style>
