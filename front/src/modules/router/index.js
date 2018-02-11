import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/auth/Login'
import Callback from '@/components/auth/Callback'
import Main from '@/components/Main'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/auth/callback',
      name: 'Callback',
      component: Callback
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    }
  ]
})
