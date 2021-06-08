<template>
<section>
  <div class="logo">
    <h1>Hostels</h1>
  </div>
  <v-row>
    <HostelCardPr
        v-for="hostelItem in hostelItems"
        :key="hostelItem.id"
        :hostel-item="hostelItem"
        class="my-2"
      />
  </v-row>
</section>
</template>
<script>
import HostelCardPr from '../components/HostelCardPr'
const apiURl = 'http://localhost:8000/api/hostels/all'
export default {
  components: {
    HostelCardPr
  },
  name: 'Hostel',
  data: () => ({
    hostelItems: []
  }),
  methods: {
    async getHostel () {
      await this.axios.get(apiURl, {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(res => {
          this.hostelItems = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log('error displaying subdivisionItems', err)
        })
    }
  },
  created () {
    this.getHostel()
  }
}
</script>
<style scoped>
  .row {
    width: 75%;
    margin: 0 auto;
  }
  .users {
    width: 450px;
    margin-bottom: 30px;
  }
  .logo {
    margin: 30px auto;
    color: darkorange;
    text-align: center;
  }
</style>
