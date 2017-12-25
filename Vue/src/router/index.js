/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Phones from '@/components/Phones'
import Exp1 from '@/components/Exp_1'
import Exp2 from '@/components/Exp_2'
import Self from '@/components/Self'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      // name: 'Exp1',
      component: Exp1
    },
    {
      path: '/register',
      // name: 'HelloWorld',
      component: Exp2
    },
    {
      path: '/phones',
      component: Phones,
    },
    {
      path: '/self',
      component: Self,
    }
  ]
})
