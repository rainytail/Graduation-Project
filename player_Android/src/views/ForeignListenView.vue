<!-- 用来列出自己收藏/保存的所有音频文件 -->

<template>
    <ContentBase>
        <div v-for="video in videos" class="card" v-bind:key="video.resourceName" style="margin-top: 10px;">
            <div class="card-body">
                <div class="row">
                    <div class="col">
                        <p>{{ video.resourceName }}</p>
                    </div>
                    <div class="col">
                        <button @click="golisten(video)" type="button" class="btn btn-primary">前往练习</button>
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

        return {
            videos,
            golisten,
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