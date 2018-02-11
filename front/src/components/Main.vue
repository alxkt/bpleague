<template>
  <div class="main">
    <nav class="uk-navbar uk-navbar-container uk-navbar-transparent uk-padding-small uk-margin">
      <div class="uk-navbar-left">
        <a class="uk-navbar-item uk-logo" href="#/main"><img src="../assets/title.png" id="logo"/></a>

        <ul class="uk-navbar-nav">
          <li class="uk-active"><a href="#">Classement</a></li>
          <li><a href="#">Mes matchs</a></li>
        </ul>
      </div>

      <div class="uk-navbar-right">
        <button class="uk-button uk-button-primary uk-margin-right" href="#modal-full" uk-toggle>Ajouter un match
        </button>
      </div>
    </nav>

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
        <table class="uk-table uk-table-divider uk-table-hover">
          <thead>
          <tr>
            <th class="uk-table-shrink">Position</th>
            <th class="uk-width-large">Nom</th>
            <th class="uk-width-small">V / D</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>1</td>
            <td>Alexis Tacnet</td>
            <td>3 / 2</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Brice Rauby</td>
            <td>1 / 3</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>


    <div id="modal-full" class="uk-modal-full" uk-modal>
      <div class="uk-modal-dialog">
        <button class="uk-modal-close-full uk-close-large" type="button" uk-close></button>
        <div class="uk-grid-collapse uk-child-width-1-2@s uk-flex-middle" uk-grid>
          <div class="uk-background-cover" uk-height-viewport id="splash"></div>
          <div class="uk-padding-large" uk-height-viewport>
            <h1 class="uk-heading-divider">Ajouter un match</h1>
            <form class="uk-form-horizontal uk-margin-large">
              <fieldset class="uk-fieldset">
                <div class="uk-margin">
                  <input class="uk-input boundary-align" type="text" placeholder="Partenaire">
                  <div uk-drop="pos: bottom-justify; boundary: .boundary-align; boundary-align: true; offset: 0">
                    <div class="uk-card uk-card-body uk-card-default">
                      <ul class="uk-list uk-list-divider">
                        <li>List item 1</li>
                        <li>List item 2</li>
                        <li>List item 3</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <h2 class="uk-heading-line uk-text-center"><span>Adversaires</span></h2>

                <div class="uk-margin">
                  <input class="uk-input" type="text" placeholder="Adversaire A">
                </div>

                <div class="uk-margin">
                  <input class="uk-input" type="text" placeholder="Adversaire B">
                </div>

                <h2 class="uk-heading-line uk-text-center"><span>Verres restants</span></h2>

                <div class="uk-margin">
                  <div class="uk-form-label">Votre équipe : {{ new_match.score_us }}</div>
                  <div class="uk-form-controls uk-form-controls-text">
                    <input class="uk-range" type="range" value="0" min="0" max="10" step="1"
                           v-model="new_match.score_us">
                  </div>
                </div>

                <div class="uk-margin">
                  <div class="uk-form-label">Vos adversaires : {{ new_match.score_them }}</div>
                  <div class="uk-form-controls uk-form-controls-text">
                    <input class="uk-range" type="range" value="0" min="0" max="10" step="1"
                           v-model="new_match.score_them">
                  </div>
                </div>
              </fieldset>

              <button class="uk-button uk-button-primary uk-margin uk-width-1-1">Ajouter le match</button>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import auth from "../modules/auth/index";

  export default {
    name: 'Main',
    data() {
      return {
        new_match: {
          ally: null,
          score_us: 0,
          score_them: 0
        }
      }
    },
    mounted() {
      auth.checkAuth();
    }
  }
</script>

<style scoped>
  .main {
    width: 100%;
  }

  #logo {
    max-height: 42px;
    margin-top: -4px;
  }

  .uk-card {
    margin: 3em auto auto;
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
