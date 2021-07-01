<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app left style="background: #dcf3ff">
      <v-list nav >
        <v-list-item style="background:snow">
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/index">Production</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item style="background:snow">
          <v-list-item-content >
            <v-list-item-title>
              <router-link to="/factory">Factories</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item style="background:snow">
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/seller">Sellers</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item style="background:snow">
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/sale">Sales</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item style="background:snow">
          <v-list-item-content>
            <v-list-item-title>
              <router-link to="/supply">Supply</router-link>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

      <v-main>
      <router-view />
    </v-main>
      </v-app>
</template>

<script>
export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: null
  })
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #425777;
}
</style>
