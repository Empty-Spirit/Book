import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// 自动引入vue相关函数
import AutoImport from 'unplugin-auto-import/vite'
// Vant 自动引入样式
import Components from 'unplugin-vue-components/vite';
import { VantResolver } from 'unplugin-vue-components/resolvers';

const path = require("path")

// https://vitejs.dev/config/
export default defineConfig({
    server: {
      // 是否开启 https
      https: false,
      // 默认localhost
      host: "0.0.0.0",
      /**
       * 端口号
       * @default 3000
       */
      port: 8080,
      // 浏览器自动打开
      open: false,
      // 本地跨域代理
      proxy: {
        "/test": {
          target: 'http://localhost:9999',
          changeOrigin: true,
          rewrite: path => path.replace(/^\/test/, '')
        }
      },
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
        '*': path.resolve('')
      }
    },
    plugins: [
      vue(),
      AutoImport({
        imports:['vue', 'vue-router', 'vuex'],
      }),
      Components({
        resolvers: [VantResolver()],
      }),
    ],
    base:'./'
  })
