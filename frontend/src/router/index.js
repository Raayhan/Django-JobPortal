import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Applications from '@/views/Applications.vue'
import SignIn from '@/views/auth/SignIn.vue'
import SignUp from '@/views/auth/SignUp.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/applications',
    name: 'applications',
    component: Applications
   
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
