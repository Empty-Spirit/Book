<template>
  <div>
    <van-sticky>
      <van-nav-bar title="首页" />
    </van-sticky>
    <Book :info="item" v-for="(item, index) in list" :key="item.name" />
  </div>
</template>

<script setup lang="ts">
import Book from "@/components/book/Index.vue";

const list = ref<any>([])

onMounted(() => {
  for(let i=0;i<10;i++){
    list.value.push({
    name: "test" + i,
    author: "author1",
    chapter: "勇敢的人",
    img: "https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg",
    lastChapter: "1222 勇敢dddddddddddddddddddddddddddddddddddddddddddd人",
  })
  }
});

</script>

<style lang="scss" scoped>
</style>
