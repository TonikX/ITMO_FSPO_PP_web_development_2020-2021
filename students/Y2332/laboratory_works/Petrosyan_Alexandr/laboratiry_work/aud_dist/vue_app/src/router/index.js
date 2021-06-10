import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "../components/Login";
import Lecturers from "../components/Lecturers";
import Home from "../components/Home";
import Disciplines from "../components/Disciplines";
import Audiences from "../components/Audiences";
import Groups from "../components/Groups";

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
        path: '/disciplines',
        name: 'Disciplines',
        component: Disciplines
    },
    {
        path: '/audiences',
        name: 'Audiences',
        component: Audiences
    },
    {
        path: '/groups',
        name: 'Groups',
        component: Groups
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
