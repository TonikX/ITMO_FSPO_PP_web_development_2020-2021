<template>
  <section>
  <div class="logo">
    <h1>Payments</h1>
  </div>
  <v-row class="row">
    <PaymentCard class="card"
        v-for="payItem in payItems"
        :key="payItem.id"
        :pay-item="payItem"
      />
  </v-row>
</section>
</template>

<script>
import PaymentCard from '../components/PaymentCard'
export default {
  components: {
    PaymentCard
  },
  name: 'Payment',
  data: () => ({
    payItems: [],
    computed: {
      id () {
        console.log('id', this.$route.params.id)
        return this.$route.params.id
      }
    }
  }),
  methods: {
    async getPayment (apiURL) {
      await this.axios.get(apiURL, {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(res => {
          this.payItems = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log('error displaying subdivisionItems', err)
        })
    }
  },
  created () {
    var apiURl = 'http://localhost:8000/api/payments/all?resident_id=' + this.$route.params.id
    this.getPayment(apiURl)
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
