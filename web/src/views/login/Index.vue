<template>
  <div>登录</div>
</template>

<script>
import { defineComponent } from 'vue'
import { useStore } from "vuex"

export default defineComponent({
  setup () {
    let store = useStore();
    console.log(store.state)
  },
})
</script>

<style lang="less" scoped>
</style>