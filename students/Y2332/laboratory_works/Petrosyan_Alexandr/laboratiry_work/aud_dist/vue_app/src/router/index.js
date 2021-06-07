import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "../components/Login";
import Lecturers from "../components/Lecturers";
import Home from "../components/Home";
import Disciplines from "../components/Disciplines";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/lecturers',
        name: 'Lecturers',
        component: Lecturers
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/disciplines',
        name: 'Disciplines',
        component: Disciplines
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
