import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/registerItem',
      name: 'registerItem',
      component: () => import('@/components/RegisterItem.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/components/Login.vue')
    },
    {
      path: '/index',
      name: 'index',
      component: () => import('@/components/Index.vue')
    },
    {
      path: '/factory',
      name: 'factory',
      component: () => import('@/components/Factory.vue')
    },
    {
      path: '/registerFactory',
      name: 'registerFactory',
      component: () => import('@/components/RegisterFactory.vue')
    },
    {
      path: '/sale',
      name: 'sale',
      component: () => import('@/components/Sale.vue')
    },
    {
      path: '/registerSale',
      name: 'registerSale',
      component: () => import('@/components/RegisterSale.vue')
    },
    {
      path: '/supply',
      name: 'supply',
      component: () => import('@/components/Supply.vue')
    },
    {
      path: '/registerSupply',
      name: 'registerSupply',
      component: () => import('@/components/RegisterSupply.vue')
    },
    {
      path: '/seller',
      name: 'seller',
      component: () => import('@/components/Seller.vue')
    },
    {
      path: '/registerSeller',
      name: 'registerSeller',
      component: () => import('@/components/RegisterSeller.vue')
    }
  ]
})
