import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Greeting from '../views/Greeting'
import Nasa from '../views/Nasa.vue'
import Hostels from '../views/Hostels'
import Room from '../views/Room'
import Users from '../views/Users'
import Payments from '../views/Payments'
import Checkin from '../views/Checkin'
import Start from '../views/Start'
import CheckinCreate from '../views/CheckinCreate'
import PayUpdate from '../views/PayUpdate'
import CreatePayment from '../views/CreatePayment'
import SignIn from '../views/SignIn'
import SignUp from '../views/SignUp'
import Profile from '../views/Profile'
import Requests from '../views/Requests'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/greeting',
    name: 'Greeting',
    component: Greeting
  },
  {
    path: '/nasa',
    name: 'Nasa',
    component: Nasa
  },
  {
    path: '/hostels',
    name: 'Hostels',
    component: Hostels
  },
  {
    path: '/rooms/:id',
    name: 'Rooms',
    component: Room
  },
  {
    path: '/users/:super',
    name: 'User',
    component: Users
  },
  {
    path: '/payments/:id',
    name: 'Payment',
    component: Payments
  },
  {
    path: '/checkin/:id',
    name: 'Checkin',
    component: Checkin
  },
  {
    path: '/start/',
    name: 'Start',
    component: Start
  },
  {
    path: '/movein/:id',
    name: 'CheckinCreate',
    component: CheckinCreate
  },
  {
    path: '/payupdate/:id',
    name: 'PayUpdate',
    component: PayUpdate
  },
  {
    path: '/paymentscreate/:id',
    name: 'PayCreate',
    component: CreatePayment
  },
  {
    path: '/signin/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signup/',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/profile/',
    name: 'profile',
    component: Profile
  },
  {
    path: '/requests/',
    name: 'requests',
    component: Requests
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
