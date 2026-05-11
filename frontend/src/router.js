import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/',     name: 'landing', component: () => import('./views/LandingView.vue') },
  { path: '/demo', name: 'demo',    component: () => import('./views/DemoView.vue') },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { top: 0 }
  },
})
