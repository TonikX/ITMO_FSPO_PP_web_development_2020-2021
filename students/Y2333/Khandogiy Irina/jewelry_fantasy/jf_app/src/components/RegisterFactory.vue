<template>
  <v-form @submit="create" ref="form" lazy-validation>
    <v-text-field v-model="factory.name" label="Name" required></v-text-field>
    <v-text-field v-model="factory.address" label="Address" required></v-text-field>
    <v-btn color="primary" type="submit">Submit</v-btn>
  </v-form>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      factory: {
        name: '',
        address: ''
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  methods: {
    create: function () {
      axios
        .post('http://127.0.0.1:8000/jewerly_fantasy/factory/', this.factory, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
        .then((response) => {
          console.log(response)
          alert('Registered Succesfuly')
          this.$router.push('/index')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
