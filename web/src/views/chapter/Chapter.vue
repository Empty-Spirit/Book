<template>
    <div>
        <van-sticky>
            <van-nav-bar left-arrow @click-left="onClickLeft" title="首页" />
        </van-sticky>
    </div>
</template>
  
<script setup lang="ts">

    const onClickLeft = () => history.back();
</script>
  
<style lang="scss" scoped></style>