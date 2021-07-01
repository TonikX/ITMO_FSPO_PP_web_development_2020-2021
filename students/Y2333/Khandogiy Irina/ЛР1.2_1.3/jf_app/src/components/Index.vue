<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in items" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="'Item ' + (i+1)"></v-card-title>
              <v-card-subtitle>
                <v-text-field v-model="item.name" label="Name" required></v-text-field>
                <v-text-field v-model="item.num" label="Num" required></v-text-field>
                <v-text-field v-model="item.type" label="Type" required disabled></v-text-field>
                <v-select v-model="item.type" label="Type" :items="types" item-text="item.type" required></v-select>

              </v-card-subtitle>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="update(item)">Submit changes</v-btn>
              </v-card-actions>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="remove(item)">Remove item</v-btn>
              </v-card-actions>
              <!--              <v-card-actions>-->
              <!--                <v-btn class="btn-success" style="color:white" text v-on:click="AddEmployer(item)">AddEmployer</v-btn>-->
              <!--              </v-card-actions>-->
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-card-actions>
      <v-card-subtitle>
        <router-link to="/registerItem" class="btn btn-sm btn-primary">Add item</router-link>
      </v-card-subtitle>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      items: [],
      types: ['Rings', 'Earrings', 'Chains', 'Bracelets', 'Pendants', 'Necklace', 'Charms', 'Another'],
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
        axios.delete(`http://127.0.0.1:8000/jewerly_fantasy/products/${e.id}/`, {
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
      axios.put(`http://127.0.0.1:8000/jewerly_fantasy/products/${e.id}/`, e, {
        headers: {
          Authorization: `${sessionStorage.getItem('auth_token')}`
        }
      })
        .then(response => {
          this.$router.push('/index')
          console.log(response)
        })
    },
    all: function () {
      axios.get('http://localhost:8000/jewerly_fantasy/products/').then((response) => {
        this.items = response.data
        console.log(response)
      })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
