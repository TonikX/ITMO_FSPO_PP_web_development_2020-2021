<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in sales" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="'Sale ' + (i+1)"></v-card-title>
              <v-card-subtitle>
                <v-text-field v-model="item.product" label="product" required></v-text-field>
                <v-text-field v-model="item.seller" label="seller" required></v-text-field>
                <v-text-field v-model="item.date" label="date" required></v-text-field>
                <v-text-field v-model="item.price" label="price" required></v-text-field>
                <v-text-field v-model="item.num" label="num" required></v-text-field>
              </v-card-subtitle>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="update(item)">Submit changes</v-btn>
              </v-card-actions>
              <v-card-actions>
                <v-btn class="btn-success" style="color:black" text v-on:click="remove(item)">Remove sale</v-btn>
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
        <router-link to="/registerSale" class="btn btn-sm btn-primary">Submit new Sale</router-link>
      </v-card-subtitle>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      sales: []
    }
  },
  created () {
    console.log('Here')
    this.all()
  },
  methods: {
    remove: function (e) {
      if (confirm('Delete ' + e.name)) {
        axios.delete(`http://127.0.0.1:8000/jewerly_fantasy/sale/${e.id}/`)
          .then((response) => {
            console.log(response)
            this.all()
          })
      }
    },
    update: function (e) {
      axios.put(`http://127.0.0.1:8000/jewerly_fantasy/sale/${e.id}/`, e, {})
        .then(response => {
          this.$router.push('/sale')
          console.log(response)
        })
    },
    all: function () {
      axios.get('http://localhost:8000/jewerly_fantasy/sale/').then((response) => {
        this.sales = response.data
        console.log(response)
      })
    }
  }
}
</script>
