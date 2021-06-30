<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <img :src="require('../assets/document.png')"
        class="my-3 img"
          contain
          height="200">

    <v-card-title>
      Наименование документа: {{checkinItem.doc_name}}
      <br>
      Дата выдачи: {{checkinItem.date_of_issue}}
    </v-card-title>

    <v-card-subtitle>
      Имя резидента: {{checkinItem.resident_id.full_name}}
      <br>
      Общежитие: {{checkinItem.room_id.hostel_id.name}}
      <br>
      Номер комнаты: {{checkinItem.room_id.id}}

    </v-card-subtitle>

    <v-card-actions>
      <v-btn v-if="new Date().getDate() == 7 && checkinItem.comment != 'request'"
        color="orange lighten-2"
        text
        @click="$router.push('/paymentscreate/' + checkinItem.id)
        $router.go()" class="v-btn"
      >
        Create Payment
      </v-btn>
      <v-btn v-if="checkinItem.doc_name != 'Checkout Doc' && checkinItem.comment != 'request'"
        color="orange lighten-2"
        text
        @click="checkOut()
        leaveRoom('http://localhost:8000/api/rooms/update/' + checkinItem.room_id.id + '/')"
      class="v-btn"
      >
        Checkout
      </v-btn>

      <v-spacer></v-spacer>
       <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
         Дата заселения: {{checkinItem.date_of_start}}
          <br>
          Дата выселения: {{checkinItem.date_of_checkout}}
          <br>
          Причина выселения: {{checkinItem.check_out_reason}}
          <br>
          Комментарии: {{checkinItem.comment}}
          <br>
          {{checkinItem.id}}
        </v-card-text>
        <v-btn v-if="checkinItem.comment == 'request'"
        color="orange lighten-2"
        text
        @click="deleteCheck()
        leaveRoom('http://localhost:8000/api/rooms/update/' + checkinItem.room_id.id + '/')"
        class="v-btn"
      >
        Delete
      </v-btn>
        <v-btn v-if="checkinItem.comment == 'request'"
        color="orange lighten-2"
        text
        @click="accept()"
        class="v-btn"
      > Accept
      </v-btn>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: 'CheckinCard',
  data: () => ({
    show: false
  }),
  props: {
    checkinItem: Object
  },
  methods: {
    async checkOut () {
      await this.axios.post('http://localhost:8000/api/checkin/create', {
        doc_num: this.checkinItem.doc_num + 1,
        date_of_issue: new Date().getFullYear().toString() + '-' + (new Date().getUTCMonth() + 1).toString() + '-' +
          new Date().getDate().toString(),
        comment: 'request',
        reason: 'Resident`s wish',
        date_of_checkout: new Date().getFullYear().toString() + '-' + (new Date().getUTCMonth() + 1).toString() + '-' +
          new Date().getDate().toString(),
        doc_name: 'Checkout Doc',
        date_of_start: new Date().getFullYear().toString() + '-' + (new Date().getUTCMonth() + 1).toString() + '-' +
          new Date().getDate().toString(),
        resident_id: this.checkinItem.resident_id.id,
        room_id: this.checkinItem.room_id.id
      },
      {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(function (response) {
          console.log(response)
          console.log('Successfully create')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    async deleteCheck () {
      await this.axios.delete('http://127.0.0.1:8000/api/checkin/delete/' + this.checkinItem.id + '/',
        {
          headers: {
            Authorization: 'Token ' + this.$cookies.get('token').toString()
          }
        }
      )
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    async leaveRoom (apiURl) {
      await this.axios.patch(apiURl, {
        busy_beds: this.checkinItem.room_id.busy_beds - 1
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
    },
    async accept () {
      await this.axios.patch('http://127.0.0.1:8000/api/checkin/update/' + this.checkinItem.id + '/', {
        comment: 'accepted'
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
  }
}
</script>

<style scoped>
.img {
    margin: 10px 35px;
  }
</style>
