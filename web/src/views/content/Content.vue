<template>
    <div class="main-content">
        <van-sticky>
            <van-nav-bar left-arrow @click-left="onClickLeft" :title="title" />
        </van-sticky>
        <div class="header">
            <span @click="pre">上一章</span>
            <span @click="go">目录</span>
            <span @click="last">下一章</span>
        </div>
        <div class="content">
            <div v-for="item in content">
                {{ item }}
            </div>
        </div>
        <div class="footer">
            <span @click="pre">上一章</span>
            <span>目录</span>
            <span @click="last">下一章</span>
        </div>
    </div>
</template>
  
<script setup lang="ts">
import { getContent } from '@/config/api'
const route = useRoute();
const router = useRouter();
let title = ref('')

let current: any = localStorage.getItem('current');
let book_local: any = localStorage.getItem('book');
let book_title: any = localStorage.getItem('book_title');

const content = ref([]);

const getContentFunc = async () => {
    const form = {
        url: route.query.url,
        order: route.query.order,
    }
    const { data } = await getContent(form);
    content.value = data.content.split('　　');
    title.value = data.title || book_title;
    console.log(data);
}

watch(route, () => {
    // url = router.currentRoute.value.query.url;
    current = localStorage.getItem('current');
    book_local = localStorage.getItem('book');
    book_title = localStorage.getItem('book_title');
    document.documentElement.scrollTop = 0;
    // this.$ref.scroll
    getContentFunc()
},{
    deep: true,
})

const pre = () => {
    if (current - 0 === 0) {
        return;
    }
    const preChapter = JSON.parse(book_local).data[current - 1];
    localStorage.setItem('current', (current - 1) + '');
    localStorage.setItem('book_title', preChapter.chapter_name);
    router.replace({
        query: {
            url: preChapter.chapter_url,
            order: route.query.order,
        }
    })
};

const go = () => {
    console.log(JSON.parse(book_local));
    router.push({
        path: '/chapter',
        query: {
            url: JSON.parse(book_local).url,
            order: route.query.order,
        }
    })
};

const last = () => {
    if (current - 0 === JSON.parse(book_local).data.length - 1) {
        return;
    }
    const lastChapter = JSON.parse(book_local).data[current - 0 + 1];
    localStorage.setItem('current', (current - 0 + 1) + '');
    localStorage.setItem('book_title', lastChapter.chapter_name);
    router.replace({
        query: {
            url: lastChapter.chapter_url,
            order: route.query.order,
        }
    })
};

onMounted(() => {
    if (!route.query.url || !route.query.order) {
        router.push({
            path: '/search',
        })
    }
    getContentFunc();
});

const onClickLeft = () => history.back();
</script>
  
<style lang="scss" scoped>
.main-content {
    padding: 0px 10px;
}

.header,
.footer {
    text-align: center;
    border-bottom: 1px solid #999;

    span {
        display: inline-block;
        margin: 20px 10px;
        cursor: pointer;

    }
}

.footer {
    border-bottom: none;
    border-top: 1px solid #999;
}

.content {
    text-indent: 2em;
    letter-spacing: 3px;
    line-height: 40px;
    text-align: left;
    font-size: 18px;
}</style>