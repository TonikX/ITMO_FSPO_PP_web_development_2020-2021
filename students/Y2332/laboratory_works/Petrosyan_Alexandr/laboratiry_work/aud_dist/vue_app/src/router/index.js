import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "../components/Login";
import Lecturers from "../components/Lecturers";
import Home from "../components/Home";
import Disciplines from "../components/Disciplines";
import Audiences from "../components/Audiences";
import Groups from "../components/Groups";
import Schedule from "../components/Schedule";

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
        component: Lecturers,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/disciplines',
        name: 'Disciplines',
        component: Disciplines,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/audiences',
        name: 'Audiences',
        component: Audiences,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/groups',
        name: 'Groups',
        component: Groups,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/schedule',
        name: 'Schedule',
        component: Schedule,
        meta: {
            requiresAuth: true
        }
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

router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requiresAuth)) {
        if (localStorage.getItem('auth_token')) {
            next()
            return
        }
        next('/')
    } else {
        next()
    }
})

export default router
