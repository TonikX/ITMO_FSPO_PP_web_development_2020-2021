<template>
  <v-card
    class="mx-auto"
    min-width="344"
  >
   <img :src="require('../assets/hostel.png')"
        class="my-3 img"
          contain
          height="200">

    <v-card-title
    @click="$router.push('/rooms/' + hostelItem.id)
    $router.go()">
      {{ hostelItem.name }}
    </v-card-title>

    <v-card-subtitle>
      Адрес:
      <br>
      Район: {{ hostelItem.address_id.city_district}}
      <br>
      Улица: {{ hostelItem.address_id.street}}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
         Корпус: {{ hostelItem.building}} Дом: {{ hostelItem.house_num }}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>
<script>
export default {
  name: 'HostelCardPr',
  data: () => ({
    show: false
  }),
  props: {
    hostelItem: Object
  }
}
</script>

<style scoped>
  a {
    text-decoration: none;
  }
  .img {
    margin: 10px 35px;
  }
</style>
