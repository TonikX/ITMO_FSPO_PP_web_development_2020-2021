<template>
    <v-form @submit="create" ref="form" lazy-validation>
      <v-text-field v-model="client.name" :counter="250" label="Name" required></v-text-field>
      <v-text-field v-model="client.address" :counter="250" label="Code" required></v-text-field>
      <v-text-field v-model="client.acc_num" :counter="250" label="Code" required></v-text-field>
      <v-btn color="primary" type="submit">Submit</v-btn>
    </v-form>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      client: {
        name: '',
        acc_num: '',
        address: 0
      },
      submitted: false
    }
  },
  methods: {
    create: function () {
      axios
        .post('http://127.0.0.1:8000/api/clients/', this.client, {
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
