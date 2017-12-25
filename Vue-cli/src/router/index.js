/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Exp1 from '@/components/Exp_1'
import Exp2 from '@/components/Exp_2'
import Thing from '@/components/Thing'
import Phones from '@/components/Phones'

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
      name: 'Exp_1',
      component: Exp1
    },
    {
      path: '/register',
      name: 'Exp_2',
      component: Exp2
    },
    {
      path: '/phones',
      // name: 'Phones',
      components: Thing
    },
  ]
})
