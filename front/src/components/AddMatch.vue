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
                  <input class="uk-input boundary-align" type="text" placeholder="Partenaire">
                  <div uk-drop="pos: bottom-justify; boundary: .boundary-align; boundary-align: true">
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
  export default {
    name: 'AddMatch',
    data() {
      return {
        new_match: {
          ally: null,
          score_us: 0,
          score_them: 0
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

  @media only screen and (max-width: 768px) {
    #splash {
      display: none;
    }
  }

</style>
