<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <img :src="require('../assets/money.png')"
        class="my-3 img"
          contain
          height="200">

    <v-card-title>
      Наименование документа: {{payItem.check_in_out_id.doc_name}}
      <br>
      Дата выдачи: {{payItem.check_in_out_id.date_of_issue}}
    </v-card-title>

    <v-card-subtitle>
      Сумма: {{payItem.amount}}
      <br>
      Статус: {{payItem.status}}
      <br>
      Дата оплаты: {{payItem.date_pay}}

    </v-card-subtitle>

    <v-card-actions>
      <v-btn v-if="payItem.status=='np' || payItem.status=='pp'"
        color="orange lighten-2"
        text
        @click="$router.push('/payupdate/' + payItem.id)
    $router.go()" class="v-btn"
      >
        Pay
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
         Дата заселения: {{payItem.check_in_out_id.date_of_start}}
          <br>
          Дата выселения: {{payItem.check_in_out_id.date_of_checkout}}
          <br>
          Причина выселения: {{payItem.check_out_reason}}
          <br>
          Комментарии: {{payItem.check_in_out_id.comment}}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: 'PaymentCard',
  data: () => ({
    show: false
  }),
  props: {
    payItem: Object
  }
}
</script>

<style scoped>
 .img{
   margin: 10px 35px;
 }
</style>
