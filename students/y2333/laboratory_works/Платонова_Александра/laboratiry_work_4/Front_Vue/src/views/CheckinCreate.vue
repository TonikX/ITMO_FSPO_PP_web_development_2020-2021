<template>
<section>
  <h1>Move in</h1>
<v-card
  elevation="10"
  class = "mx-auto"
  max-width="50%"
  >
  <v-form
    ref="form"
    :style="{'padding':'20px'}"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="doc_num"
      label="Doc number"
      required
    ></v-text-field>
     <v-text-field
      v-model="date_of_issue"
      type="date"
      label="Date of issue"
      required
    ></v-text-field>
    <v-text-field
      v-model="comment"
      label="Comment"
      required
    ></v-text-field>
    <v-text-field
      v-model="reason"
      label="Check out reason"
      required
    ></v-text-field>
    <v-text-field
      v-model="date_of_checkout"
      type="date"
      label="Date of checkout"
      required
    ></v-text-field>
    <v-text-field
      v-model="doc_name"
      label="Doc name"
      required
    ></v-text-field>
    <v-text-field
      v-model="date_of_start"
      type="date"
      label="Date of start"
      required
    ></v-text-field>
    <v-select
      v-model="resident_id"
      :items="residents"
      :rules="[v => !!v || 'Resident is required']"
      item-text="username"
      item-value="id"
      label="Resident id"
      required
    ></v-select>
    <v-text-field
    v-model="room_id"
      label="room_id"
      required>
    </v-text-field>
    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="pushCheckin('http://localhost:8000/api/checkin/create')
     getRoom('http://localhost:8000/api/rooms/all?id=', room_id)"
    >
      Submit
    </v-btn>
    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset Form
    </v-btn>
  </v-form>
  <v-btn @click="$router.push('/start/')
    $router.go()">Back to start menu</v-btn>
</v-card>
</section>
</template>
<script>

const URlRES = 'http://localhost:8000/api/residents/all'
export default {
  name: 'CheckinCreate',
  data: () => ({
    doc_num: '',
    date_of_issue: new Date().getDate(),
    comment: 'request',
    reason: '',
    date_of_checkout: new Date().getDate(),
    doc_name: '',
    date_of_start: new Date().getDate(),
    resident_id: null,
    room_id: '',
    residents: [],
    room: [],
    busy_beds: 1,
    computed: {
      id () {
        console.log('id', this.$route.params.id)
        return this.$route.params.id
      }
    }
  }),
  methods: {
    async pushCheckin (apiURl) {
      await this.axios.post(apiURl, {
        doc_num: this.doc_num,
        date_of_issue: this.date_of_issue,
        comment: this.comment,
        reason: this.reason,
        date_of_checkout: this.date_of_checkout,
        doc_name: this.doc_name,
        date_of_start: this.date_of_start,
        resident_id: this.resident_id,
        room_id: this.room_id
      },
      {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    reset () {
      console.log(this.resident_id)
      this.$refs.form.reset()
    },
    async getResident () {
      await this.axios.get(URlRES)
        .then(res => {
          this.residents = res.data
          console.log(this.resident_id)
        })
        .catch(err => {
          console.log('error displaying residentItems', err)
        })
    },
    async getRoom (apiURL, id) {
      await this.axios.get(apiURL + id, {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(res => {
          this.room = res.data[0]
          this.busy_beds = this.room.busy_beds
          this.updateRoom('http://localhost:8000/api/rooms/update/' + id + '/')
          console.log(res.data)
          console.log(this.room.busy_beds)
        })
        .catch(err => {
          console.log('error displaying subdivisionItems', err)
        })
    },
    async updateRoom (apiURl) {
      await this.axios.patch(apiURl, {
        busy_beds: this.busy_beds + 1
      },
      {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(function (response) {
          console.log(response)
          console.log('Successfully update')
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  created () {
    this.getResident()
    this.room_id = this.$route.params.id
    this.doc_name = 'Checkin Document'
    this.doc_num = Math.floor(Math.random() * 10000)
    // this.getRoom('http://localhost:8000/api/rooms/all?id=', this.room_id)
  }
}
</script>
