<template>
  <v-form @submit="create" ref="form" lazy-validation>
    <v-text-field v-model="item.name" label="Name" required></v-text-field>
    <v-text-field v-model="item.num" label="Num" required></v-text-field>
    <v-select v-model="item.type" label="Type" :items="types" item-text="type" item-value='id' required></v-select>

    <v-btn color="primary" type="submit">Submit</v-btn>
  </v-form>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      types: [
        { id: '1', type: 'Rings' },
        { id: '2', type: 'Earrings' },
        { id: '3', type: 'Chains' },
        { id: '4', type: 'Bracelets' },
        { id: '5', type: 'Pendants' },
        { id: '6', type: 'Necklace' },
        { id: '7', type: 'Charms' },
        { id: '8', type: 'Another' }
      ],
      type: ['Rings', 'Earrings', 'Chains', 'Bracelets', 'Pendants', 'Necklace', 'Charms', 'Another'],
      item: {
        name: '',
        num: '',
        type: '',
        photo: null
      },
      submitted: false
    }
  },
  created () {
    this.loadItems()
  },
  methods: {
    loadItems () {
      axios.get('http://localhost:8000/jewerly_fantasy/products/', {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      }).then((response) => {
        this.playgrounds = response.data
        console.log(response)
      })
    },
    create: function () {
      axios
        .post('http://127.0.0.1:8000/jewerly_fantasy/products/', this.item, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
        .then((response) => {
          console.log(response)
          this.$router.push('/registerItem')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
