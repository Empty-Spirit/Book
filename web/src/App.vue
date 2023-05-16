<template>
  <router-view />
  <van-back-top right="10px" bottom="60px" />
</template>

<script setup lang="ts">
  // import api from "./config/api";

  // let router = useRouter();
  // let route = useRoute();
  // let store = useStore();
  // let params = {};
  // api.user.login(params).then(res => {
  //   console.log(res, "dddd");
  // });
  // console.log(router.push, route.query, store);
  // console.log(process.env.NODE_ENV);
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
