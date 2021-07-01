<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in sellers" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="'Seller ' + (i+1)"></v-card-title>
              <v-card-subtitle>
                <v-text-field v-model="item.surname" label="Surname" required></v-text-field>
                <v-text-field v-model="item.name" label="Name" required></v-text-field>
                <v-text-field v-model="item.patr" label="Patr" required></v-text-field>
                <v-text-field v-model="item.address" label="Address" required></v-text-field>
                <v-date-picker v-model="item.birth" label="Birthday" required></v-date-picker>
                <v-text-field v-model="item.salary" label="Salary" required></v-text-field>
                <v-text-field v-model="item.exp" label="Experience" required></v-text-field>
                <v-text-field v-model="item.education" label="Education" required></v-text-field>
              </v-card-subtitle>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="update(item)">Submit changes</v-btn>
              </v-card-actions>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="remove(item)">Remove employee</v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-card-actions>
      <v-card-subtitle>
        <router-link to="/registerSeller" class="btn btn-sm btn-primary">Add seller</router-link>
      </v-card-subtitle>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      sellers: []
    }
  },
  created () {
    console.log('Here')
    this.all()
  },
  methods: {
    remove: function (e) {
      if (confirm('Delete ' + e.name)) {
        axios.delete(`http://127.0.0.1:8000/jewerly_fantasy/seller/${e.id}/`, {
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
      axios.put(`http://127.0.0.1:8000/jewerly_fantasy/seller/${e.id}/`, e, {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      })
        .then(response => {
          this.$router.push('/seller')
          console.log(response)
        })
    },
    all: function () {
      axios.get('http://localhost:8000/jewerly_fantasy/seller/').then((response) => {
        this.sellers = response.data
        console.log(response)
      })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
