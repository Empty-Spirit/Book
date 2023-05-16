import { createApp } from 'vue'
import App from './App.vue'
import router from "./router";
import { vuexStore } from "./store"
import '@vant/touch-emulator';

// 移动端适配
import 'lib-flexible/flexible.js';

// 引入全局样式
import '@/assets/scss/index.scss';

// 全局引入按需引入UI库 vant
import { vantPlugins } from './plugins/vant.js';

//全局公共组件
import components from './plugins/components.js';

createApp(App).use(router).use(vuexStore).use(vantPlugins).use(components).mount('#app')
