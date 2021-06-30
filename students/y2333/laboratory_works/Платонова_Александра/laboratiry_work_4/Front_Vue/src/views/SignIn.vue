<template>
    <section>
    <h1>SignIn</h1>
        <v-card
  elevation="10"
  class = "mx-auto"
  max-width="50%"
  >
  <v-form
    ref="form"
    :style="{'padding':'20px'}"
  >
  <v-text-field
      v-model="username"
      label="Username"
      required
    ></v-text-field>
    <v-text-field
      v-model="password"
      type="password"
      label="Password"
      required
    ></v-text-field>
    <v-btn
      color="success"
      class="mr-4"
      @click="pushUser('http://localhost:8000/auth/token/login/')"
    >
      Submit
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset
    </v-btn>
    <a href='/signup'>Sign Up</a>
  </v-form>
  <v-card-text text-color="error">
      {{ message }}
  </v-card-text>
        </v-card>
    </section>
</template>
<script>
export default {
  name: 'SignIn',
  data: () => ({
    username: '',
    password: '',
    message: ''
  }),
  methods: {
    async pushUser (url) {
      await this.axios.post(url, {
        password: this.password,
        username: this.username
      })
        .then(response => {
          this.$cookies.set('token', response.data.auth_token)
          console.log(this.$cookies.get('token'))
          this.message = 'Ok'
          this.$router.push('/start')
          this.$router.go()
        })
        .catch(error => {
          console.log(error)
          this.$cookies.set('token', 'error')
        })
    },
    reset () {
      this.$refs.form.reset()
    }
  }
}
</script>
