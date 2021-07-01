<template>
  <v-form @submit="create" ref="form" lazy-validation>
    <v-date-picker v-model="sale.date" :counter="250" label="Date" required></v-date-picker>
    <v-text-field v-model="sale.price" :counter="250" label="Price" required></v-text-field>
    <v-text-field v-model="sale.num" :counter="250" label="Num" required></v-text-field>
    <v-select v-if="sellers" v-model="sale.seller" :items="sellers" label="Seller"
              item-text="name" item-value="id" required></v-select>
    <v-select v-if="products" v-model="sale.product" :items="products" label="Item"
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
      sellers: [],
      sale: {
        product: null,
        seller: null,
        date: '',
        price: '',
        num: ''
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  created () {
    this.loadItems()
    this.loadSellers()
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
    loadSellers () {
      axios.get('http://localhost:8000/jewerly_fantasy/seller/', {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      }).then((response) => {
        this.sellers = response.data
        console.log(response)
      })
    },
    create: function () {
      axios
        .post('http://127.0.0.1:8000/jewerly_fantasy/sale/', this.sale, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
        .then((response) => {
          console.log(response)
          alert('Registered Succesfuly')
          this.$router.push('/sale')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
