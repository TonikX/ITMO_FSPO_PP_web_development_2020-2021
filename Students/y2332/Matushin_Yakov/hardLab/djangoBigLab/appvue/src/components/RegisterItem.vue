<template>
    <v-form @submit="create" ref="form" lazy-validation>
      <v-text-field v-model="production.name" :counter="250" label="Name" required></v-text-field>
      <v-text-field v-model="production.code" :counter="250" label="Code" required></v-text-field>
      <v-text-field v-model="production.unit" :counter="250" label="Unit" required></v-text-field>
      <v-text-field v-model="production.amount" :counter="250" label="Amount" required></v-text-field>
      <v-text-field v-model="production.minimum" :counter="250" label="Minimum" required></v-text-field>
      <v-text-field v-model="production.desc" :counter="250" label="Description" required></v-text-field>
      <v-btn color="primary" type="submit">Submit</v-btn>
    </v-form>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      production: {
        name: '',
        code: '0',
        unit: 'kek',
        amount: 5,
        minimum: 1,
        desc: ''
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  methods: {
    create: function () {
      axios
        .post('http://127.0.0.1:8000/api/items/', this.production, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
        .then((response) => {
          console.log(response)
          alert('Registered Succesfuly')
          this.$router.push('/')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
