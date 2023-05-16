<template>
  <div>
    <van-sticky>
      <van-search
        id="input"
        v-model="value"
        show-action
        clearable
        placeholder="请输入搜索关键词"
        clear-trigger="always"
        @search="onSearch"
      >
        <template #action>
          <div
            @click="
              () => {
                onSearch(value);
              }
            "
          >
            搜索
          </div>
        </template>
      </van-search>
    </van-sticky>
    <div class="search-list">
      <span class="history" v-for="(item, index) in list">
        {{ item.key }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { getTest } from "@/config/api";
const value = ref("");
const list = ref<any>([]);

const onSearch = (val: string) => {
  console.log(val);
};

const getList = async () => {
  const result = await getTest();
  console.log(result);
  for (let i = 1; i < 10; i++) {
    list.value.push({
      key: "search" + i,
    });
  }
};

onMounted(() => {
  getList();
});
</script>

<style lang="scss" scoped>
.search-list{
  width: 100%;
  .history{
    display: inline-block;
    height: 20px;
    line-height: 20px;
    padding: 0px 5px;
    border-radius: 3px;
    background: #ddd;
    margin: 10px;
  }
}
</style>
