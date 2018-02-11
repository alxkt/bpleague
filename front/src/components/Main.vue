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

    <add-match></add-match>
  </div>
</template>

<script>
  import AddMatch from './AddMatch';

  export default {
    name: 'Main',
    data() {
      return {
      }
    },
    components: {
      AddMatch
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

</style>
