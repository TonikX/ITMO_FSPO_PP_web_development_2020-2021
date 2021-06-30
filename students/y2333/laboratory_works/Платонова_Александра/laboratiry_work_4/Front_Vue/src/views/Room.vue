<template>
<section>
  <div class="logo">
    <h1>Rooms in hostel</h1>
  </div>
  <v-row class="row">
    <RoomsCard
        v-for="roomItem in roomItems"
        :key="roomItem.id"
        :room-item="roomItem"
        class="card"
      />
  </v-row>
</section>
</template>
<script>
import RoomsCard from '../components/RoomsCard'

export default {
  components: {
    RoomsCard
  },
  name: 'Room',
  data: () => ({
    roomItems: [],
    computed: {
      id () {
        console.log('id', this.$route.params.id)
        return this.$route.params.id
      }
    }
  }),
  methods: {
    async getRoom (apiURL) {
      await this.axios.get(apiURL, {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(res => {
          this.roomItems = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log('error displaying subdivisionItems', err)
        })
    }
  },
  created () {
    var apiURl = 'http://localhost:8000/api/rooms/all?hostel_id=' + this.$route.params.id
    this.getRoom(apiURl)
  }
}
</script>
<style scoped>
  .row {
    width: 75%;
    margin: 0 auto;
  }
  .card {
    width: 450px;
    margin-bottom: 30px;
  }
  .logo {
    margin: 30px auto;
    color: darkorange;
    text-align: center;
  }
</style>
