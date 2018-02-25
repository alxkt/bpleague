<template>
  <v-slide-y-transition>
    <v-card color="secondary" dark v-if="active">
      <v-card-title primary-title>
        <div>
          <div class="headline">Un de vos matchs a été ajouté le {{ notification.match.date.day }}-{{ notification.match.date.month }}-{{ notification.match.date.year }} à {{ notification.match.date.hour }}:{{ notification.match.date.minute }}</div>
          <span class="grey--text subheading">
            [{{ notification.match.playerA.first_name }} {{ notification.match.playerA.last_name }} et
            {{ notification.match.playerB.first_name }} {{ notification.match.playerB.last_name }}]
            {{ notification.match.scoreAB }} - {{ notification.match.scoreCD }}
            [{{ notification.match.playerC.first_name }} {{ notification.match.playerC.last_name }} et
            {{ notification.match.playerD.first_name }} {{ notification.match.playerD.last_name }}]
          </span>
        </div>
      </v-card-title>
      <v-card-actions>
        <v-btn flat color="primary" @click="validateNotification">Confirmer</v-btn>
        <v-btn flat color="error" @click="contestMatch">Contester</v-btn>
        <v-spacer></v-spacer>
        <v-btn icon @click.native="show = !show">
          <v-icon>{{ show ? 'keyboard_arrow_up' : 'keyboard_arrow_down' }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-slide-y-transition>
        <v-card-text v-if="show" class="px-4">
          Date : {{ notification.match.date.day }}-{{ notification.match.date.month }}-{{ notification.match.date.year }} {{ notification.match.date.hour }}:{{ notification.match.date.minute }}<br/>
          Joueur A : {{ notification.match.playerA.first_name }} {{ notification.match.playerA.last_name }}<br/>
          Joueur B : {{ notification.match.playerB.first_name }} {{ notification.match.playerB.last_name }}<br/>
          Joueur C : {{ notification.match.playerC.first_name }} {{ notification.match.playerC.last_name }}<br/>
          Joueur D : {{ notification.match.playerD.first_name }} {{ notification.match.playerD.last_name }}<br/>
          Score équipe AB : {{ notification.match.scoreAB }}<br/>
          Score équipe CD : {{ notification.match.scoreCD }}<br/>
          Joueur ayant enregistré le match : {{ notification.match.issuer.first_name }} {{ notification.match.issuer.last_name }}
        </v-card-text>
      </v-slide-y-transition>
    </v-card>
  </v-slide-y-transition>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Notification',
    data() {
      return {
        show: false,
        active: true
      }
    },
    props: ['notification', 'snackbar'],
    methods: {
      validateNotification: function() {
        let vw = this;
        axios.delete(process.env.API_URL + '/notifications/' + this.notification.id)
          .then(function (response) {
            vw.active = false;
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      contestMatch: function() {
        let vw = this;
        axios.post(process.env.API_URL + '/matchs/' + this.notification.match.id, {contestation: true})
          .then(function (response) {
            vw.snackbar.text = 'Match contesté avec succés.';
            vw.snackbar.show = true;
            vw.validateNotification();
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    }
  }
</script>
