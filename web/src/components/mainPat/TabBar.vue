<template>
  <div>
    <van-tabbar fixed route v-model="active" @change="onChange">
      <van-tabbar-item
        v-for="(item, index) in props.data"
        :to="item.to"
        :name="item.name"
        :key="index"
        :icon="item.icon"
        >{{ item.title }}</van-tabbar-item
      >
    </van-tabbar>
  </div>
</template>

<script lang="ts">
export default {
  name: "TabBar",
};
</script>

<script setup lang="ts">
import { reactive, ref } from "vue";

interface tabProps {
  data?: [
    {
      title: string;
      to: string;
      name: string;
      icon: string;
    }
  ];
}

const props = defineProps<tabProps>();
console.log(props.data, "props.data");

const emit = defineEmits(["chang"]);

const active = ref("home");

const onChange = (value: string) => {
  // console.log(value,'value');

  emit("chang", value);
};
</script>

<style lang="scss" scoped></style>
