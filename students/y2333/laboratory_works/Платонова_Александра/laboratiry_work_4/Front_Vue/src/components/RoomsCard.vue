<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >

    <img :src="require('../assets/room.png')"
        class="my-3 img"
          contain
          height="200">

    <v-card-title>

      Номер комнаты: {{ roomItem.id}}
      <br>
      Этаж: {{ roomItem.floor }}
    </v-card-title>

    <v-card-subtitle>
      Всего мест: {{roomItem.beds}}
      <br>
      Занято: {{ roomItem.busy_beds}}
      <br>
      Плащадь: {{roomItem.area}}

    </v-card-subtitle>
    <a v-if="roomItem.beds > roomItem.busy_beds" @click="$router.push('/movein/' + roomItem.id)
    $router.go()" class="button">Move in</a>
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
         Университет: {{roomItem.hostel_id.name}}
         Адрес: {{roomItem.hostel_id.address_id.city_district}} р-н, ул. {{roomItem.hostel_id.address_id.street}}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>
<script>

export default {
  name: 'RoomsCard',
  data: () => ({
    show: false
  }),
  props: {
    roomItem: Object
  }
}
</script>

<style scoped>
  .img {
    margin: 10px 35px;
  }
  a {
   margin: 16px;
   display:  inline-block;
   text-decoration: none;
   font-weight: 900;
   color: #000;
   padding: 5px;
   border-radius: 10px;
  }
  a:hover{
   background: orange;
   color: #fff;
  }

</style>
