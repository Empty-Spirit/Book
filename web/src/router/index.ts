import { createRouter, RouteRecordRaw, createWebHistory } from "vue-router";

import Login from '../views/login/Index.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: "Login",
    component: Login
  }
]

const index = createRouter({
  history: createWebHistory(),
  routes
})

export default index;