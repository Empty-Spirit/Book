import { createRouter, RouteRecordRaw, createWebHistory } from "vue-router";
import { vuexStore } from "@/store";

// import Login from '../views/login/Index.vue'
// 通过Vite的import.meta.glob()方法实现自动化导入路由
const mainRouterModules = import.meta.glob("../layout/*.vue");
const viewRouterModules = import.meta.glob("../views/**/*.vue");

// 子路由
const childRoutes = Object.keys(viewRouterModules).map((path: any) => {
  const childName = path.match(/\.\.\/views\/(.*)\.vue$/)[1].split("/")[1];
  return {
    path: `/${childName.toLowerCase()}`,
    name: childName,
    component: viewRouterModules[path],
  };
});

// 根路由
const rootRoutes = Object.keys(mainRouterModules).map((path: any) => {
  const name = path.match(/\.\.\/layout\/(.*)\.vue$/)[1].toLowerCase();
  const routePath = `/${name}`;
  if (routePath === "/index") {
    return {
      path: "/",
      name,
      redirect: "/home",
      component: mainRouterModules[path],
      children: childRoutes,
    };
  }
});

const routes: any = rootRoutes;

const index = createRouter({
  history: createWebHistory(),
  routes,
});

// 路由拦截
index.beforeEach((to, from, next) => {
  vuexStore.commit('isLoading', false);
  // store.commit('changeActiveIndex', iconMap[to.path]);
  // store.commit('changeRule', to.path);
  // store.commit('delTip', iconMap[to.path])
  next();
});

export default index;
