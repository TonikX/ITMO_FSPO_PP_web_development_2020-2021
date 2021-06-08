<template>
<section>
  <h1>Pay</h1>
<v-card
  elevation="10"
  class = "mx-auto"
  max-width="50%"
  >
  <v-form
    ref="form"
    :style="{'padding':'20px'}"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="amount"
      label="Amount"
      required
    ></v-text-field>
     <v-text-field
      v-model="status"
      type="text"
      :counter="1"
      label="Status"
      required
    ></v-text-field>
    <v-text-field
      v-model="date_pay"
      type="date"
      label="Date of pay"
      required
    ></v-text-field>
<!--    <v-select-->
<!--      v-model="check_in_out_id"-->
<!--      :items="checkins"-->
<!--      :rules="[v => !!v || 'Checkin is required']"-->
<!--      item-text="check_in_out_id"-->
<!--      item-value="id"-->
<!--      label=this.$route.params.id-->
<!--      required-->
<!--    ></v-select>-->
    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="pushPay('http://localhost:8000/api/payments/update/' + $route.params.id + '/')"
    >
      Submit
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset($route.params.id)"
    >
      Reset Form
    </v-btn>
  </v-form>
  <v-btn @click="$router.push('/start/')
    $router.go()">Back to start menu</v-btn>
</v-card>
</section>
</template>
<script>
export default {
  name: 'PayCreate',
  data: () => ({
    amount: '',
    status: '',
    date_pay: new Date(),
    check_in_out_id: null
  }),
  methods: {
    async pushPay (apiURl) {
      await this.axios.put(apiURl, {
        amount: this.amount,
        status: 'p',
        date_pay: this.date_pay,
        check_in_out_id: this.check_in_out_id
      }, {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    reset (id) {
      console.log(this.status)
      this.$refs.form.reset()
      this.getPay('http://localhost:8000/api/payments/update/' + id + '/')
    },
    async getPay (URL) {
      await this.axios.get(URL)
        .then(res => {
          this.amount = res.data.amount
          this.status = 'p'
          this.check_in_out_id = res.data.check_in_out_id
          this.date_pay = res.data.date_pay
          console.log(this.data)
        })
        .catch(err => {
          console.log('error displaying residentItems', err)
        })
    }
  },
  created () {
    var URl = 'http://localhost:8000/api/payments/all/' + this.$route.params.id + '/'
    this.getPay(URl)
  }
}
</script>
