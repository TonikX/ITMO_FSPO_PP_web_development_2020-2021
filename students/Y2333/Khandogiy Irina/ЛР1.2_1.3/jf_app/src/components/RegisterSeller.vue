<template>
  <v-form @submit="create" ref="form" lazy-validation>
    <v-text-field v-model="seller.surname" label="surname" required></v-text-field>
    <v-text-field v-model="seller.patr" label="patr" required></v-text-field>
    <v-text-field v-model="seller.name" label="name" required></v-text-field>
    <v-text-field v-model="seller.address" label="address" required></v-text-field>
    <v-date-picker v-model="seller.birth" label="birth" required></v-date-picker>
    <v-text-field v-model="seller.salary" label="salary" required></v-text-field>
    <v-text-field v-model="seller.exp" label="exp" required></v-text-field>
    <v-text-field v-model="seller.education" label="education" required></v-text-field>
    <v-btn color="primary" type="submit">Submit</v-btn>
  </v-form>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      seller: {
        surname: '',
        patr: '',
        name: '',
        address: '',
        birth: '',
        salary: '',
        exp: '',
        education: ''
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  methods: {
    create: function () {
      axios
        .post('http://127.0.0.1:8000/jewerly_fantasy/seller/', this.seller, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
        .then((response) => {
          console.log(response)
          alert('Registered Succesfuly')
          this.$router.push('/seller')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
