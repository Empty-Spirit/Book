<template>
  <div>
    <van-sticky>
      <van-search id="input" v-model="searchValue" show-action clearable placeholder="请输入搜索关键词" clear-trigger="always"
        @search="onSearch">
        <template #action>
          <div @click="() => {
              onSearch(searchValue);
            }
            ">
            搜索
          </div>
        </template>
      </van-search>
    </van-sticky>
    <div v-if="!is_search" class="search-list">
      <span class="history" v-for="(item, index) in list">
        {{ item.key }}
      </span>
    </div>
    <Book 
      v-else 
      :right="false" 
      :info="item" 
      v-for="(item, index) in book_list" 
      :key="item.name" 
      @click="goInfo(item)"
    />
  </div>
</template>

<script setup lang="ts">
import Book from "@/components/book/Index.vue";
import { getBook } from "@/config/api";
import { vuexStore }  from '@/store'
const router = useRouter();

const search = computed(() => vuexStore.state.search);

const searchValue = ref("");
const list = ref<any>([]);
const book_list = ref<any>([]);
const is_search = ref<any>(false);

const onSearch = async (val: string) => {
  const form = {
    name: val,
    page: 1,
  }

  const { data } = await getBook(form);
  book_list.value = data;
  is_search.value = true;
  vuexStore.commit("changeSearchList", {
    key: val,
    list: data,
  });
};

const getList = async () => {
  for (let i = 1; i < 10; i++) {
    list.value.push({
      key: "search" + i,
    });
  }
};

const goInfo = (item:any) => {
  console.log(item);
  router.push({
    path: '/chapter',
  })
};

onMounted(() => {
  getList();
  if(search.value.list.length){
    book_list.value = search.value.list;
    is_search.value = true;
    searchValue.value = search.value.key;
  }
});
</script>

<style lang="scss" scoped>
.search-list {
  width: 100%;

  .history {
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
