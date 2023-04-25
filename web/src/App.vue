<template>
  <router-view />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";
import api from "./config/api";

export default defineComponent({
  name: "App",
  setup() {
    let router = useRouter();
    let route = useRoute();
    let store = useStore();
    let params = {};
    api.user.login(params).then(res => {
      console.log(res, "dddd");
    });
    console.log(router.push, route.query, store);
    console.log(process.env.NODE_ENV);
    return {};
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
