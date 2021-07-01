<template>
  <v-form @submit="setMyLogin" ref="form" lazy-validation>
    <v-text-field  v-model="username" label="Username"></v-text-field>
    <v-text-field  v-model="password" type="password" label="Password"></v-text-field>
    <v-btn color="primary" type="submit">Login</v-btn>
  </v-form>
</template>

<script>
import $ from 'jquery'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    setMyLogin: function () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/token/login/',
        type: 'POST',
        data: {
          username: this.username,
          password: this.password
        },
        success: (response) => {
          console.log(response.auth_token)
          // alert("Welcome!")
          const token = response.auth_token
          sessionStorage.setItem('auth_token', 'token ' + token)
          this.$router.push({ name: 'index' })
        },
        error: (response) => {
          console.log(response)
          if (response.status === 400) {
            alert('Login')
          }
        }
      })
    }
  }
}
</script>
