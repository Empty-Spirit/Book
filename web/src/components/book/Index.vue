<template>
  <div class="book">
    <van-swipe-cell>
      <div class="main">
        <div class="left">
          <van-image :src="info.img" class="img">
            <template v-slot:error>加载失败</template>
          </van-image>
        </div>
        <div class="right">
          <div class="title">{{ info.name }}</div>
          <div class="author">{{ info.author }}</div>
          <div class="author">{{ info.chapter }}</div>
          <div class="author">{{ info.lastChapter }}</div>
        </div>
      </div>
      <template #right v-if="right">
        <van-button square text="详情" type="primary" class="delete-button" />
        <van-button square text="删除" type="danger" class="delete-button" />
      </template>
    </van-swipe-cell>
  </div>
</template>

<script setup lang="ts">
const { info, right } = withDefaults(
  defineProps<{
    info: any;
    right?: boolean;
  }>(),
  {
    right: true,
  }
)

const goInfo = (item: Number) => {
  console.log(item);
};
</script>

<style lang="scss" scoped>
.goods-card {
  margin: 0;
  background-color: white;
}

.delete-button {
  height: 100%;
}

.main {
  padding: 10px 5px;
  display: flex;

  .left {
    display: inline-block;
    width: 88px;
    height: 88px;

    .img {
      width: 100%;
      height: 100%;
      border-radius: 8px;
      overflow: hidden;
    }
  }

  .right {
    flex: 1;
    display: inline-block;
    vertical-align: top;
    margin-left: 10px;
    overflow: hidden;
    padding-right: 20px;

    >div {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin: 5px 0px;
    }

    .title {
      font-weight: 400;
      font-size: 18px;
      margin-bottom: 10px;
    }

    .author {
      color: #666;
      font-size: 14px;
    }

    .last-chapter {
      color: #666;
      font-size: 14px;
      bottom: 2px;
    }
  }
}</style>
