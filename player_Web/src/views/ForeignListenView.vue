<!-- 用来列出自己收藏/保存的所有音频文件 -->

<template>
    <ContentBase>
        <div v-for="video in videos" class="card" v-bind:key="video.resourceName" style="margin-top: 10px;">
            <div class="card-body">
                <div class="row">
                    <div class="col-9">
                        <p>{{ video.resourceName }}</p>
                    </div>
                    <div class="col-3">
                        <button @click="golisten(video)" style="margin-right: 15px" type="button" class="btn btn-primary">前往练习</button>
                        <button @click="download(video)" type="button" class="btn btn-primary">下载音频</button>
                    </div>
                </div>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '../components/ContentBase.vue';
import { useStore } from 'vuex';
import $ from 'jquery';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: "ForeignListenView",
    components: {
        ContentBase,
    },
    data() {
        return {
            items: [], // 原始数据列表
            paginatedItems: [] // 分页后的数据列表
        };
    },
    methods: {
        handlePagination(items, page) {
            this.paginatedItems = items.slice((page - 1) * 10, page * 10);
        }
    },
    setup() {
        let store = useStore();
        let videos = ref([]);
        let router = useRouter();

        // 接口，获取用户的所有保存收藏的音频
        $.ajax({
            url: "http://81.70.183.49:8000/vueApi/getforeignlisten",
            type: "get",
            async: false,
            success(resp) {
                let getvideos = resp.videos;
                videos.value = getvideos;
                console.log(videos.value);
            }
        });

        // 把需要的听力资源存到vuex中
        const golisten = (video) => {
            store.commit("changeListen", {
                ...video,
                type: 'cloud',
            });
            router.replace({ name: "player" });
        };

        const download = (audio) => {
            const url = 'http://81.70.183.49:8000/static/videos/' + audio.resourceUrl; // 替换为你的后端 URL
    
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url);
            // blob数据即为大二进制数据，用于存储音频、视频、图像等
            xhr.responseType = 'blob'; // 告诉 XMLHttpRequest 返回的数据类型是 Blob 对象
            
            xhr.onload = function() {
                if (xhr.status === 200) {
                    // 创建一个 <a> 元素
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(xhr.response);
                    link.download = audio.resourceUrl; // 设置下载文件的名称
                    
                    // 模拟点击这个 <a> 元素来触发下载
                    link.click();
                } else {
                    console.error('Request failed with status:', xhr.status);
                }
            };
            
            xhr.send();
        };

        return {
            videos,
            golisten,
            download,
        }
    }
}
</script>

<style scoped>
.card {
    user-select: none;
    cursor: pointer; 
    -webkit-transition: all .5s; 
    -moz-transition: all .5s; 
    -ms-transition: all .5s; 
    -o-transition: all .5s; 
    transition: all .5s;
    background-color: white;
}
.card:hover {
    background-color: #F6F7F5;
}
</style>