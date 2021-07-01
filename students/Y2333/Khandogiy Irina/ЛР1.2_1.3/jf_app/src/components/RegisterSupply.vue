<template>
  <v-form @submit="create" ref="form" lazy-validation>
    <v-date-picker v-model="supplier.post_date" :counter="250" label="Date" required></v-date-picker>
    <v-text-field v-model="supplier.amount" :counter="250" label="Amount" required></v-text-field>
    <v-text-field v-model="supplier.price" :counter="250" label="Price" required></v-text-field>
    <v-select v-if="factories" v-model="supplier.factory" :items="factories" label="Factory"
              item-text="name" item-value="id" required></v-select>
    <v-select v-if="products" v-model="supplier.product" :items="products" label="Item"
              item-text="name" item-value="id" required></v-select>
    <v-btn color="primary" type="submit">Submit</v-btn>
  </v-form>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      products: [],
      factories: [],
      supplier: {
        product: null,
        factory: null,
        post_date: '',
        amount: '',
        price: ''
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  created () {
    this.loadFactories()
    this.loadItems()
  },
  methods: {
    loadItems () {
      axios.get('http://localhost:8000/jewerly_fantasy/products/', {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      }).then((response) => {
        this.products = response.data
        console.log(response)
      })
    },
    loadFactories () {
      axios.get('http://localhost:8000/jewerly_fantasy/factory/', {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      }).then((response) => {
        this.factories = response.data
        console.log(response)
      })
    },
    create: function () {
      axios
        .post('http://127.0.0.1:8000/jewerly_fantasy/supply/', this.supplier, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
        .then((response) => {
          console.log(response)
          alert('Registered Succesfuly')
          this.$router.push('/supply')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
