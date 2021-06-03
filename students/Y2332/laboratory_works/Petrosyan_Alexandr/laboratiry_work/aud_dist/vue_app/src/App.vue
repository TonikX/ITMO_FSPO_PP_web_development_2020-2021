<template>
  <v-app>
    <v-app-bar app>
        <v-btn to="/">Главная</v-btn>
        <v-btn to="/lecturers">Преподаватели</v-btn>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
