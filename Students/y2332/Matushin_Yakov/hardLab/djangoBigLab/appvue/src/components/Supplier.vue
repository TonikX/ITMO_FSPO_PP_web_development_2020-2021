<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in suppliers" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="item.name"></v-card-title>
              <v-card-subtitle>
                <v-expansion-panels v-model="panel" :disabled="disabled">
                  <v-expansion-panel>
                    <v-expansion-panel-header>Details</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <b>Supplier Address:</b> {{ item.address}}
                      <br />
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card-subtitle>
              <v-card-actions>
               <router-link :to="{name: 'editEmployer', params: { id: item.id }}" class="btn btn-sm btn-primary">Edit</router-link>
              </v-card-actions>
              <v-card-actions>
               <v-btn class="btn-success" style="color:black" text v-on:click="remove(item)">Delete</v-btn>
              </v-card-actions>
<!--              <v-card-actions>-->
<!--                <v-btn class="btn-success" style="color:white" text v-on:click="AddEmployer(item)">AddEmployer</v-btn>-->
<!--              </v-card-actions>-->
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      suppliers: []
    }
  },
  created () {
    console.log('Here')
    this.all()
  },
  methods: {
    remove: function (e) {
      if (confirm('Delete ' + e.name)) {
        axios.delete(`http://127.0.0.1:8000/api/suppliers/${e.id}`, {
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
    all: function () {
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
    }
  }
}
</script>
