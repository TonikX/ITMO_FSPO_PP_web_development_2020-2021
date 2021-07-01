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
      path: '/login',
      name: 'login',
      component: () => import('@/components/Login.vue')
    },
    {
      path: '/registerEmployer',
      name: 'registerEmployer',
      component: () => import('@/components/RegisterEmployer.vue')
    },
    {
      path: '/editEmployer/:id',
      name: 'editEmployer',
      component: () => import('@/components/EditEmployer.vue')
    },
    {
      path: '/index',
      name: 'index',
      component: () => import('@/components/Index.vue')
    },
    {
      path: '/production',
      name: 'production',
      component: () => import('@/components/Production.vue')
    },
    {
      path: '/registerItem',
      name: 'registerItem',
      component: () => import('@/components/RegisterItem.vue')
    },
    {
      path: '/editItem/:id',
      name: 'editItem',
      component: () => import('@/components/EditItem.vue')
    },
    {
      path: '/clients',
      name: 'clients',
      component: () => import('@/components/Clients.vue')
    },
    {
      path: '/registerClient',
      name: 'registerClient',
      component: () => import('@/components/RegisterClient.vue')
    },
    {
      path: '/editClient/:id',
      name: 'editClient',
      component: () => import('@/components/EditEmployer.vue')
    },
    {
      path: '/suppliers',
      name: 'suppliers',
      component: () => import('@/components/Supplier.vue')
    },
    {
      path: '/registerSupplier',
      name: 'registerSupplier',
      component: () => import('@/components/RegisterSupplier.vue')
    },
    {
      path: '/editSupplier/:id',
      name: 'editSupplier',
      component: () => import('@/components/EditEmployer.vue')
    },
    {
      path: '/batches',
      name: 'batches',
      component: () => import('@/components/Batch.vue')
    },
    {
      path: '/registerBatch',
      name: 'registerBatch',
      component: () => import('@/components/RegisterBatch.vue')
    },
    {
      path: '/editBatch/:id',
      name: 'editBatch',
      component: () => import('@/components/EditItem.vue')
    }
  ]
})
