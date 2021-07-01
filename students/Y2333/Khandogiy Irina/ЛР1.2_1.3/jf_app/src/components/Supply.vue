<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in suppliers" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="'Supply ' + (i+1)"></v-card-title>
              <v-card-subtitle>
                <v-text-field v-model="item.post_date" label="Date" required></v-text-field>
                <v-text-field v-model="item.amount" label="Amount" required></v-text-field>
                <v-text-field v-model="item.price" label="Price" required></v-text-field>
                <v-text-field v-model="item.factory" label="Factory" required></v-text-field>
                <v-text-field v-model="item.product" label="Product" required></v-text-field>
              </v-card-subtitle>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="update(item)">Submit changes</v-btn>
              </v-card-actions>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="remove(item)">Remove Supply</v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-card-actions>
      <v-card-subtitle>
        <router-link to="/registerSupply" class="btn btn-sm btn-primary">Add Supply</router-link>
      </v-card-subtitle>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      suppliers: [],
      submitted: false
    }
  },
  created () {
    console.log('Here')
    this.all()
  },
  methods: {
    remove: function (e) {
      if (confirm('Delete ' + e.name)) {
        axios.delete(`http://127.0.0.1:8000/jewerly_fantasy/supply/${e.id}/`, {
          headers: {
            Authorization: `${sessionStorage.getItem('auth_token')}`
          }
        })
          .then((response) => {
            console.log(response)
            this.all()
          })
      }
    },
    update: function (e) {
      axios.put(`http://127.0.0.1:8000/jewerly_fantasy/supply/${e.id}/`, e, {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      })
        .then(response => {
          this.$router.push('/supply')
          console.log(response)
        })
    },
    all: function () {
      axios.get('http://localhost:8000/jewerly_fantasy/supply/').then((response) => {
        this.suppliers = response.data
        console.log(response)
      })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
