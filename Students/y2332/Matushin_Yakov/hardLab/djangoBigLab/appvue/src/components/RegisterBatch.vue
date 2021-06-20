<template>
  <v-form @submit="create" ref="form" lazy-validation>
    <v-select v-if="suppliers" v-model="batch.supplier" :items="suppliers" :counter="250" label="Supplier"
              item-text="name" item-value="id" required></v-select>
    <v-select v-if="clients" v-model="batch.client" :items="clients" :counter="250" label="Client" item-text="name"
              item-value="id" required></v-select>
    <v-select v-if="employers" v-model="batch.employer" :items="employers" :counter="250" label="Employer"
              item-text="name" item-value="id" required></v-select>
    <v-select v-if="items" v-model="batch.production" :items="items" :counter="250" label="Item" item-text="name"
              item-value="id" required></v-select>
    <v-text-field v-model="batch.amount" :counter="250" label="Amount" required></v-text-field>
    <v-date-picker v-model="batch.supply_date" :counter="250" label="Supply Date" required></v-date-picker>
    <v-date-picker v-model="batch.delivery_date" :counter="250" label="Delivery Date" required></v-date-picker>
    <v-text-field v-model="batch.price" :counter="250" label="Price" required></v-text-field>
    <v-btn color="primary" type="submit">Submit</v-btn>
  </v-form>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      suppliers: [],
      clients: [],
      employers: [],
      items: [],
      batch: {
        supplier: null,
        client: null,
        employer: null,
        production: null,
        supply_date: '',
        delivery_date: '',
        amount: '',
        price: '',
        isFulfilled: false
      },
      admin_id: '',
      admin_password: '',
      submitted: false
    }
  },
  created () {
    this.loadEmployers()
    this.loadClients()
    this.loadItems()
    this.loadSuppliers()
  },
  methods: {
    loadEmployers () {
      console.log('Getting data')
      axios.get('http://localhost:8000/api/employers/', {
        auth: {
          username: 'djangouser',
          password: 'pass12345'
        }
      }).then((response) => {
        this.employers = response.data
        console.log(response)
      })
    },
    loadClients () {
      console.log('Getting data')
      axios.get('http://localhost:8000/api/clients/', {
        auth: {
          username: 'djangouser',
          password: 'pass12345'
        }
      }).then((response) => {
        this.clients = response.data
        console.log(response)
      })
    },
    loadItems () {
      console.log('Getting data')
      axios.get('http://localhost:8000/api/items/', {
        auth: {
          username: 'djangouser',
          password: 'pass12345'
        }
      }).then((response) => {
        this.items = response.data
        console.log(response)
      })
    },
    loadSuppliers () {
      console.log('Getting data')
      axios.get('http://localhost:8000/api/suppliers/', {
        auth: {
          username: 'djangouser',
          password: 'pass12345'
        }
      }).then((response) => {
        this.suppliers = response.data
        console.log(response)
      })
    },
    create: function () {
      axios
        .post('http://127.0.0.1:8000/api/batches/', this.batch, {
          auth: {
            username: this.admin_id,
            password: this.admin_password
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
