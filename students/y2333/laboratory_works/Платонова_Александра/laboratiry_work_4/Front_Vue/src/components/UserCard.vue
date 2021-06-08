<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <img :src="require('../assets/user.png')"
        class="my-3 img"
          contain
          height="200">

    <v-card-title  @click="$router.push('/payments/' + userItem.id)
    $router.go()">
      Имя: {{userItem.full_name}}
    </v-card-title>

    <v-card-subtitle>
      UserName: {{userItem.username}}
      <br>
      Супер пользователь: {{userItem.is_superuser}}
      <br>
      Email: {{userItem.email}}
      <br>
      Дети: {{ userItem.children}}
      <br>
    </v-card-subtitle>

    <v-card-actions>
      <v-btn v-if="$route.params.super == 1"
        color="orange lighten-2"
        @click="$router.push('/payments/' + userItem.id)
    $router.go()" class="v-btn"
      text>
        Show payments
      </v-btn>
      <v-btn v-if="$route.params.super == 1"
        color="orange lighten-2"
        @click="$router.push('/checkin/' + userItem.id)
    $router.go()" class="v-btn"
      text>
        Show documents
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
          Паспорт: {{userItem.passport}}
          <br>
          Учебное заведение: {{ userItem.educational_institution}}
          <br>
          Работа: {{userItem.organization_id.name}}
          <br>
          Адрес организации:
          {{userItem.organization_id.legal_address}}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: 'UserCard',
  data: () => ({
    show: false
  }),
  props: {
    userItem: Object
  }
}
</script>

<style scoped>
.img {
    margin: 10px 35px;
  }
.v-btn{
  font-size: 10px;
}
</style>
