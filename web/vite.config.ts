import { ConfigEnv, UserConfigExport } from 'vite'
import vue from '@vitejs/plugin-vue'
const resolve = require("path")

// https://vitejs.dev/config/
export default ({ command }: ConfigEnv): UserConfigExport => {
  return {
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
      open: true,
      // 本地跨域代理
      proxy: {
        "/test": {
          target: 'http://stzbxinghe.com/stzbxinghe/php/',
          changeOrigin: true,
          rewrite: path => path.replace(/^\/test/, '')
        }
      },
    },
    plugins: [vue()]
  }
}
