<template>
  <section>
  <div class="logo">
    <h1>Checkin-Checkout Documents</h1>
  </div>
  <v-row class="row">
    <CheckinCard class="card"
        v-for="checkinItem in checkinItems"
        :key="checkinItem.id"
        :checkin-item="checkinItem"
      />
  </v-row>
</section>
</template>

<script>
import CheckinCard from '../components/CheckinCard'
export default {
  components: {
    CheckinCard
  },
  name: 'Requests',
  data: () => ({
    checkinItems: []
  }),
  methods: {
    async getCheckin (apiURL) {
      await this.axios.get(apiURL, { headers: { Authorization: 'Token ' + this.$cookies.get('token').toString() } })
        .then(res => {
          this.checkinItems = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log('error displaying subdivisionItems', err)
        })
    }
  },
  created () {
    var apiURl = 'http://localhost:8000/api/checkin/all?comment=request'
    this.getCheckin(apiURl)
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
