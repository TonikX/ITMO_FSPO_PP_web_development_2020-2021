<template>
    <v-form @submit="create" ref="form" lazy-validation>
      <v-text-field v-model="employer.name" :counter="250" label="Name" required></v-text-field>
      <v-text-field v-model="employer.code" :counter="250" label="Code" required></v-text-field>
      <v-text-field v-model="employer.pass_data" :counter="250" label="Pass Data" required></v-text-field>
      <v-btn color="primary" type="submit">Submit</v-btn>
    </v-form>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      employer: {
        name: '',
        code: 0,
        pass_data: 1
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  methods: {
    create: function () {
      axios
        .post('http://127.0.0.1:8000/api/employers/', this.employer, {
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
