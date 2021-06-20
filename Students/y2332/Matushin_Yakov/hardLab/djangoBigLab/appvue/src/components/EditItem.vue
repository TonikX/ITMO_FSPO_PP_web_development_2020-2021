<template>
  <v-container>
    <v-form @submit="update" ref="form" lazy-validation>
      <v-text-field v-model="item.name" :counter="250" label="Name" required></v-text-field>
      <v-text-field v-model="item.code" :counter="250" label="Code" required></v-text-field>
      <v-text-field v-model="item.unit" :counter="250" label="Pass Data" required></v-text-field>
      <v-text-field v-model="item.amount" :counter="250" label="Name" required></v-text-field>
      <v-text-field v-model="item.minimum" :counter="250" label="Code" required></v-text-field>
      <v-text-field v-model="item.desc" :counter="250" label="Pass Data" required></v-text-field>
      <v-btn color="primary" type="submit">Submit</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      item: null,
      submitted: false
    }
  },
  mounted: function () {
    axios
      .get('http://127.0.0.1:8000/api/items/' + this.$route.params.id, {
        auth: {
          username: 'djangouser',
          password: 'pass12345'
        }
      })
      .then((response) => {
        console.log(response.data)
        this.item = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    update: function (e) {
      axios.put(`http://127.0.0.1:8000/api/items/${this.item.id}/`, this.item, {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      })
        .then(response => {
          this.$router.push('/')
        })
    }
  }
}
</script>
