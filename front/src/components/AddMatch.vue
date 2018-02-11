<template>
  <div class="add-match uk-animation-toggle">
    <div id="modal-full" class="uk-modal-full uk-animation-slide-top" uk-modal>
      <div class="uk-modal-dialog">
        <button class="uk-modal-close-full uk-close-large" type="button" uk-close></button>
        <div class="uk-grid-collapse uk-child-width-1-2@s uk-flex-middle" uk-grid>
          <div class="uk-background-cover" uk-height-viewport id="splash"></div>
          <div class="uk-padding-large" uk-height-viewport>
            <h1 class="uk-heading-divider">Ajouter un match</h1>
            <form class="uk-form-horizontal uk-margin-large">
              <fieldset class="uk-fieldset">
                <div class="uk-margin">
                  <input class="uk-input boundary-align" type="text" placeholder="Partenaire" v-model="ally.name">
                  <div uk-drop="mode: click; pos: bottom-justify; boundary: .boundary-align; boundary-align: true">
                    <div class="uk-card uk-card-body uk-card-default" v-if="search.length > 0 && ally.id == null">
                      <ul class="uk-list uk-list-divider">
                        <li v-for="ally_search in search" v-on:click="select(ally, ally_search)">{{ ally_search.first_name }} {{ ally_search.last_name }}</li>
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
                        <li v-for="adversary_search in search" v-on:click="select(adversaryA, adversary_search)">{{ adversary_search.first_name }} {{ adversary_search.last_name }}</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <div class="uk-margin">
                  <input class="uk-input" type="text" placeholder="Adversaire B" v-model="adversaryB.name">
                  <div uk-drop="mode: click; pos: bottom-justify; boundary: .boundary-align; boundary-align: true">
                    <div class="uk-card uk-card-body uk-card-default" v-if="search.length > 0 && adversaryB.id == null">
                      <ul class="uk-list uk-list-divider">
                        <li v-for="adversary_search in search" v-on:click="select(adversaryB, adversary_search)">{{ adversary_search.first_name }} {{ adversary_search.last_name }}</li>
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

  export default {
    name: 'AddMatch',
    data() {
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
        search: []
      }
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
        this.getUsers(newAlly);
      },
      adversaryA_name: function (newAdversary) {
        this.getUsers(newAdversary);
      },
      adversaryB_name: function (newAdversary) {
        this.getUsers(newAdversary);
      }
    },
    methods: {
      getUsers: _.debounce(
        function (search) {
          let addMatch = this;

          axios.get(process.env.API_URL + '/users?search=' + search)
            .then(function (response) {
              addMatch.search = response.data;
            })
            .catch(function (error) {
              console.log(error);
            });
        },
        500
      ),
      select: function(field, search) {
        field.name = search.first_name + ' ' + search.last_name;
        field.id = search.id;
      },
      addMatch: function () {
        console.log(this.ally);
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

  @media only screen and (max-width: 768px) {
    #splash {
      display: none;
    }
  }

</style>
