<template>
    <div>
        <van-sticky>
            <van-nav-bar left-arrow @click-left="onClickLeft" :title="bookInfo.name" />
        </van-sticky>
        <van-cell v-for="(item, index) in bookInfo.data" :title="item.chapter_name" @click="goInfo(item, index)" is-link />
    </div>
</template>
  
<script setup lang="ts">
    import { getChapter } from '@/config/api'
    const route = useRoute();
    const router = useRouter();
    const bookInfo = ref<any>({});

    const getChapterList = async () => {
        const form = {
            url: route.query.url,
            order: route.query.order,
        }

        const { data } = await getChapter(form);
        bookInfo.value = data;
        data.url = route.query.url;
        localStorage.setItem('book', JSON.stringify(data));
        console.log(data);
    }

    const goInfo = (item: any, index: number) => {
        localStorage.setItem("current", index+'');
        localStorage.setItem('book_title', item.chapter_name);
        
        router.push({
            path: '/content',
            query: {
                url: item.chapter_url,
                order: route.query.order,
            }
        })
    };

    const onClickLeft = () => history.back();

    onMounted(() => {
        getChapterList();
    });
</script>
  
<style lang="scss" scoped></style>