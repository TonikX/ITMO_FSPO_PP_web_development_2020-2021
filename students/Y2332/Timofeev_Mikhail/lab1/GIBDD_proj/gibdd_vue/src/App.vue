<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-btn to="/" text>
        GIBDD
      </v-btn>

      <v-btn to="/bodies" text>
        Bodies
      </v-btn>

      <v-btn to="/engines" text>
        Engines
      </v-btn>

      <v-btn to="/models" text>
        Models
      </v-btn>

      <v-btn to="/lOwners" text>
        LOwners
      </v-btn>

      <v-btn to="/pOwners" text>
        POwners
      </v-btn>

      <v-btn to="/cars" text>
        Cars
      </v-btn>

      <v-btn to="/inspectors" text>
        Inspectors
      </v-btn>

      <v-btn to="/away-list" text>
        Aways
      </v-btn>

      <v-btn to="/watch-list" text>
        Watches
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
          v-if="!this.isAuthorized()"
          to="/sign-up"
          class="mr-3"
          color="success"
      >
        Sign up
      </v-btn>

      <v-btn
          v-if="!this.isAuthorized()"
          to="/log-in"
          color="success"
      >
        Log in
      </v-btn>

      <v-btn
          v-if="this.isAuthorized()"
          class=""
          color="error"
          @click="logOut"
      >
        Log out
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AuthorizationService from "@/services/AuthorizationService";
import DataService from "@/services/DataService";

  export default {
    name: 'App',
    methods: {
      isAuthorized() {
        return sessionStorage.getItem('auth_token') != null
            && sessionStorage.getItem('auth_token') !== "null";
      },

      logOut() {
        AuthorizationService.logOut()
          .then((response) => {
            console.log(response);
            DataService.setToken(null);
            sessionStorage.setItem('auth_token', null);
            this.$router.push({name: "home"});
            this.$forceUpdate();
          })
          .catch((e) => {
            console.log(e);
          });
      },
    }
  };
</script>
