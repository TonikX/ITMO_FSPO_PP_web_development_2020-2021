import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home'
import ServicesIndex from '../views/services/ServicesIndex'
import ClientsIndex from '../views/clients/ClientsIndex'
import DoctorsIndex from '../views/doctors/DoctorsIndex'
import DoctorServices from '../views/doctor_services/DoctorServicesIndex'
import TicketIndex from '../views/tickets/TicketIndex'
import Login from '../views/Login'
import axios from "axios";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
        meta: { requiresAuth: true }
    },
    {
            path: '/login',
            name: 'login',
            component: Login,
    },
    {
        path: '/services',
        name: 'services',
        component: ServicesIndex,
        meta: { requiresAuth: true }
    },
    {
        path: '/clients',
        name: 'clients',
        component: ClientsIndex,
        meta: { requiresAuth: true }
    },
    {
        path: '/doctors',
        name: 'doctors',
        component: DoctorsIndex,
        meta: { requiresAuth: true }
    },
    {
        path: '/doctor-services',
        name: 'doctor_services',
        component: DoctorServices,
        meta: { requiresAuth: true }
    },
    {
        path: '/tickets',
        name: 'tickets',
        component: TicketIndex,
        meta: { requiresAuth: true }
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (axios.defaults.headers.common['Authorization'] === undefined) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
})

export default router
