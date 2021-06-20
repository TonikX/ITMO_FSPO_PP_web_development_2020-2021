<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in batches" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="i+1"></v-card-title>
              <v-card-subtitle>
                <v-expansion-panels v-model="panel" :disabled="disabled">
                  <v-expansion-panel>
                    <v-expansion-panel-header>Details</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <b>Item:</b> {{ item.production}}
                      <br />
                      <b>Supplier:</b> {{ item.supplier}}
                      <br />
                      <b>Client:</b> {{ item.client}}
                      <br />
                      <b>Employer:</b> {{ item.employer}}
                      <br />
                      <b>Delivery Date:</b> {{ item.delivery_date}}
                      <br />
                      <br />
                      <b>Supply Date:</b> {{ item.supply_date}}
                      <br />
                      <br />
                      <b>Amount:</b> {{ item.amount}}
                      <br />
                      <br />
                      <b>Price:</b> {{ item.price}}
                      <br />
                      <br />
                      <b>Fulfilled:</b> {{ item.isFulfilled}}
                      <br />
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card-subtitle>
              <v-card-actions>
               <v-btn class="btn-success" style="color:black" text v-on:click="remove(item)">Delete</v-btn>
              </v-card-actions>
              <v-card-actions>
               <v-btn class="btn-success" style="color:black" text v-on:click="update(item)">Submit</v-btn>
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
      batches: [],
      batch: null,
      admin_id: '',
      admin_password: '',
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
        axios.delete(`http://127.0.0.1:8000/api/batches/${e.id}/`, {
          auth: {
            username: 'djangouser',
            password: 'pass12345'
          }
        })
          .then((response) => {
            console.log(response)
            this.all()
          })
      }
    },
    update: function (e) {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/api/batches/${e.id}/`,
        data: {
          supplier: e.supplier,
          client: e.client,
          employer: e.employer,
          production: e.production,
          supply_date: e.supply_date,
          delivery_date: e.delivery_date,
          amount: e.amount,
          price: e.price,
          isFulfilled: true
        }
      })
    },
    all: function () {
      console.log('Getting data')
      axios.get('http://localhost:8000/api/batches/', {
        auth: {
          username: 'djangouser',
          password: 'pass12345'
        }
      }).then((response) => {
        this.batches = response.data
        console.log(response)
      })
    }
  }
}
</script>
