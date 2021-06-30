<template>
  <section>
  <div class="logo">
    <h1>Users</h1>
  </div>
  <v-row class="row">
    <UserCard class="users"
        v-for="userItem in userItems"
        :key="userItem.id"
        :user-item="userItem"
      />
  </v-row>
</section>
</template>

<script>
import UserCard from '../components/UserCard'
const apiURl = 'http://localhost:8000/api/residents/all'
export default {
  components: {
    UserCard
  },
  name: 'User',
  data: () => ({
    userItems: [],
    computed: {
      super () {
        console.log('super', this.$route.params.super)
        return this.$route.params.super
      }
    }
  }),
  methods: {
    async getUser () {
      await this.axios.get(apiURl, {
        headers: {
          Authorization: 'Token ' + this.$cookies.get('token').toString()
        }
      })
        .then(res => {
          this.userItems = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log('error displaying', err)
        })
    }
  },
  created () {
    this.getUser()
  }
}
</script>

<style scoped>
  .row {
    width: 75%;
    margin: 0 auto;
  }
  .users {
    width: 450px;
    margin-bottom: 30px;
  }
  .logo {
    margin: 30px auto;
    color: darkorange;
    text-align: center;
  }
</style>
