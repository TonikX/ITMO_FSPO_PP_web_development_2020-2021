<template>
  <div class="wrapper">
 <div class="card">
  <div class="face face1">
   <div class="content">
    <img :src="require('../assets/hostels.svg')"
        class="my-3 img"
          contain
          height="200">
    <h3>Hostel</h3>
   </div>
  </div>
  <div class="face face2">
   <div class="content">
    <p @click="$router.push('/rooms/' + '???')
    $router.go()">Click here to watch all hostels</p>

    <a href="http://localhost:8080/hostels">Click me</a>
   </div>
  </div>
 </div>
 <div class="card">
  <div class="face face1">
   <div class="content">
    <img :src="require('../assets/user.svg')"
        class="my-3 img"
          contain
          height="200">
    <h3>Users</h3>
   </div>
  </div>
  <div class="face face2">
   <div class="content">
    <p >Click here to watch all users</p>
    <a  @click="$router.push('/users/' + Number(is_superuser))
        $router.go()">Click me</a>
   </div>
  </div>
 </div>
 <div class="card">
  <div class="face face1">
   <div class="content">
   <img :src="require('../assets/doc.svg')"
        class="my-3 img"
          contain
          height="200">
    <h3>Documents</h3>
   </div>
  </div>
  <div class="face face2">
   <div class="content">
    <p>Click here to watch all documents</p>
    <a @click="$router.push('/checkin/' + id)
        $router.go()">Click me</a>
   </div>
  </div>
 </div>
     <div class="card">
  <div class="face face1">
   <div class="content">
    <img :src="require('../assets/money.svg')"
        class="my-3 img"
          contain
          height="200">
    <h3>Payments</h3>
   </div>
  </div>
  <div class="face face2">
   <div class="content">
    <p>Click here to watch all payments</p>
    <a @click="$router.push('/payments/' + id)
        $router.go()">Click me</a>
   </div>
  </div>
 </div>
    <div class="card" v-if="is_superuser">
  <div class="face face1">
   <div class="content">
    <img :src="require('../assets/doc.svg')"
        class="my-3 img"
          contain
          height="200">
    <h3>Requests</h3>
   </div>
  </div>
  <div class="face face2">
   <div class="content">
    <p>Click here to watch all requests</p>
    <a @click="$router.push('/requests/')
        $router.go()">Click me</a>
   </div>
  </div>
 </div>
<div class="card">
  <div class="face face1">
   <div class="content">
    <img :src="require('../assets/user.svg')"
        class="my-3 img"
          contain
          height="200">
    <h3>Me</h3>
   </div>
  </div>
  <div class="face face2">
   <div class="content">
    <ul>
      <br>
      <li>Reg. num: {{this.registration_num}}</li>
      <li>Username: {{this.username}}</li>
      <li>Email: {{this.email}}</li>
      <li>Children: {{this.children}}</li>
      <li>Full name: {{this.full_name}}</li>
    </ul>
     <a href="http://localhost:8080/profile/">Update data</a>
   </div>
  </div>
 </div>
</div>
</template>

<script>

export default {
  data: () => ({
    show: false,
    id: '',
    registration_num: '',
    full_name: '',
    children: '',
    email: '',
    is_superuser: false,
    username: '',
    passport: '',
    message: '',
    educational_institution: '',
    organization_id: '',
    password: ''
  }),
  name: 'Start',
  methods: {
    async getUpdateItems (URl_) {
      await this.axios.get(URl_, { headers: { Authorization: 'Token ' + this.$cookies.get('token').toString() } })
        .then(res => {
          this.id = res.data.id
          this.registration_num = res.data.registration_num
          this.children = res.data.children
          this.username = res.data.username
          this.password = res.data.password
          this.getUserInfo('http://localhost:8000/api/residents/all/' + this.id + '/')
        })
        .catch(err => {
          console.log('error displaying subdivisionItem', err)
        })
    },
    async getUserInfo (URl_) {
      await this.axios.get(URl_, { headers: { Authorization: 'Token ' + this.$cookies.get('token').toString() } })
        .then(res => {
          this.id = res.data.id
          this.registration_num = res.data.registration_num
          this.full_name = res.data.full_name
          this.children = res.data.children
          this.passport = res.data.passport
          this.email = res.data.email
          this.is_superuser = res.data.is_superuser
          this.username = res.data.username
          this.password = res.data.password
        })
        .catch(err => {
          console.log('error displaying subdivisionItem', err)
        })
    }
  },
  created () {
    if (this.$cookies.get('token') === 'error') {
      this.$router.push('/signin')
    }
    var URl_ = 'http://localhost:8000/auth/users/me/'
    this.getUpdateItems(URl_)
  }
}
</script>

<style scoped>
  * {
    margin: 0 auto;
  }
  body{
 margin: 0 auto;
 padding: 0;
 min-height: 100vh;
 background: #333;
 display: flex;
 justify-content: center;
 align-items: center;
 font-family: consolas;
}

.wrapper{
 width: 1000px;
 position: relative;
 display: flex;
 flex-wrap: wrap;
 justify-content: space-around;
}

.wrapper .card{
 position: relative;
 cursor: pointer;
  margin-left: 30px;
}

.wrapper .card .face{
 width: 300px;
 height: 200px;
 transition: 0.5s;
}

.wrapper .card .face.face1{
 position: relative;
 background: #333;
 display: flex;
 justify-content: center;
 align-items: center;
 z-index: 1;
 transform: translateY(100px);
}

.wrapper .card:hover .face.face1{
 background: darkorange;
 transform: translateY(0);
}

.wrapper .card .face.face1 .content{
 opacity: 0.2;
 transition: 0.5s;
}

.wrapper .card:hover .face.face1 .content{
 opacity: 1;
}

.wrapper .card .face.face1 .content img{
 max-width: 100px;
}

.wrapper .card .face.face1 .content h3{
 margin: 10px 0 0;
 padding: 0;
 color: #fff;
 text-align: center;
 font-size: 1.5em;
}

.wrapper .card .face.face2{
 position: relative;
 background: #fff;
 display: flex;
 justify-content: center;
 align-items: center;
 padding: 20px;
 box-sizing: border-box;
 box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
 transform: translateY(-100px);
}

.wrapper .card:hover .face.face2{
 transform: translateY(0);
}

.wrapper .card .face.face2 .content p{
 margin: 0;
 padding: 0;
}

.wrapper .card .face.face2 .content a{
 margin: 15px 0 0;
 display:  inline-block;
 text-decoration: none;
 font-weight: 900;
 color: #333;
 padding: 5px;
 border: 1px solid #333;
}

.wrapper .card .face.face2 .content a:hover{
 background: #333;
 color: #fff;
}
</style>
