import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Applications from '@/views/Applications.vue'
import SignIn from '@/views/auth/SignIn.vue'
import SignUp from '@/views/auth/SignUp.vue'
import Category from '@/views/Category.vue'
import JobDetails from '@/views/JobDetails.vue'
import JobApplication from '@/views/JobApplication.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/applications',
    name: 'applications',
    component: Applications,
    meta: {
      requireLogin:true
    }
   
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
  },
  
  {
    path: '/:category_slug/',
    name: 'Category',
    component: Category
  },
  {
    path: '/:category_slug/:job_slug',
    name: 'JobDetails',
    component: JobDetails
  },
  {
    path: '/:category_slug/:job_slug/apply',
    name: 'JobApplication',
    component: JobApplication,
    props: true,
    meta: {
      requireLogin:true
    }
 }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'SignIn', query: { to: to.path } });
  }
  else {
    next()
  }
})
export default router
