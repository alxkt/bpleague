<template>
  <div class="add-match uk-animation-toggle">
    <div id="modal-full" class="uk-modal-full uk-animation-slide-top" uk-modal>
      <div class="uk-modal-dialog">
        <button class="uk-modal-close-full uk-close-large" type="button" uk-close></button>
        <div class="uk-grid-collapse uk-child-width-1-2@s uk-flex-middle" uk-grid>
          <div class="uk-background-cover uk-visible@s" uk-height-viewport id="splash"></div>
          <div class="uk-padding-large" uk-height-viewport>
            <h1 class="uk-heading-divider">Ajouter un match</h1>
            <form class="uk-form-horizontal uk-margin-large">
              <fieldset class="uk-fieldset">
                <div class="uk-margin">
                  <input class="uk-input boundary-align" type="text" placeholder="Partenaire" v-model="ally.name">
                  <div uk-drop="mode: click; pos: bottom-justify; boundary: .boundary-align; boundary-align: true">
                    <div class="uk-card uk-card-body uk-card-default" v-if="search.length > 0 && ally.id == null">
                      <ul class="uk-list uk-list-divider">
                        <li v-for="ally_search in search" v-on:click="select(ally, ally_search)">{{ ally_search.name }}</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <h2 class="uk-heading-line uk-text-center"><span>Adversaires</span></h2>

                <div class="uk-margin">
                  <input class="uk-input" type="text" placeholder="Adversaire A" v-model="adversaryA.name">
                  <div uk-drop="mode: click; pos: bottom-justify; boundary: .boundary-align; boundary-align: true">
                    <div class="uk-card uk-card-body uk-card-default" v-if="search.length > 0 && adversaryA.id == null">
                      <ul class="uk-list uk-list-divider">
                        <li v-for="adversary_search in search" v-on:click="select(adversaryA, adversary_search)">{{ adversary_search.name }}</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <div class="uk-margin">
                  <input class="uk-input" type="text" placeholder="Adversaire B" v-model="adversaryB.name">
                  <div uk-drop="mode: click; pos: bottom-justify; boundary: .boundary-align; boundary-align: true">
                    <div class="uk-card uk-card-body uk-card-default" v-if="search.length > 0 && adversaryB.id == null">
                      <ul class="uk-list uk-list-divider">
                        <li v-for="adversary_search in search" v-on:click="select(adversaryB, adversary_search)">{{ adversary_search.name }}</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <h2 class="uk-heading-line uk-text-center"><span>Verres restants</span></h2>

                <div class="uk-margin">
                  <div class="uk-form-label">Votre équipe : {{ score_us }}</div>
                  <div class="uk-form-controls uk-form-controls-text">
                    <input class="uk-range" type="range" value="0" min="0" max="10" step="1"
                           v-model="score_us">
                  </div>
                </div>

                <div class="uk-margin">
                  <div class="uk-form-label">Vos adversaires : {{ score_them }}</div>
                  <div class="uk-form-controls uk-form-controls-text">
                    <input class="uk-range" type="range" value="0" min="0" max="10" step="1"
                           v-model="score_them">
                  </div>
                </div>
              </fieldset>

              <button class="uk-button uk-button-primary uk-margin uk-width-1-1" v-on:click="addMatch()">Ajouter le match</button>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios';
  import _ from 'lodash';
  import UIkit from 'uikit';

  import matchs from '../modules/matchs';
  import auth from '../modules/auth';

  function init() {
    return {
        score_us: 0,
        score_them: 0,
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

          axios.get(process.env.API_URL + '/users?search=' + search)
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
            })
            .catch(function (error) {
              console.log(error);
            });
        },
        500
      ),
      select: function(field, search) {
        field.name = search.name;
        field.id = search.id;
      },
      addMatch: function () {
        const me_id = auth.user.profile.id;
        let vw = this;
        if (this.ally.id == null) {
          UIkit.notification("Vous n'avez pas mis de partenaire !", {status: 'danger'});
        } else if (this.adversaryA.id == null || this.adversaryB.id == null) {
          UIkit.notification("Vous n'avez pas mis d'adversaire !", {status: 'danger'});
        } else if (this.score_us === 0 && this.score_them === 0 ) {
          UIkit.notification("Le score indiqué est un peu chelou.", {status: 'danger'});
        } else {
          matchs.addMatch(me_id, this.ally.id, this.adversaryA.id, this.adversaryB.id, this.score_us, this.score_them).then(() => {
            UIkit.modal('#modal-full').hide();
            UIkit.notification("<span uk-icon='icon: check'></span> Match ajouté.", {status: 'primary'});
            Object.assign(this.$data, init());
            vw.$root.$emit('updateLeaderboard', true);
          }).catch(() => {});
        }
      }
    }
  }
</script>

<style scoped>
  .add-match {
    width: 100%;
  }

  #splash {
    background-image: url('../assets/images/splash.jpg');
  }

</style>
