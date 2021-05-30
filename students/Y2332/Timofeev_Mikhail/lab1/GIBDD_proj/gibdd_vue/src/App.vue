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
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
  };
</script>
