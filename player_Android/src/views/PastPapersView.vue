<!-- 用来列出自己收藏/保存的所有音频文件 -->

<template>
    <ContentBase>
        <div class="container text-center" style="">
            <div class="row">
                <div class="card">
                    <div class="card-body">
						<div class="d-flex flex-row mb-3">
						  <div class="p-2">
							  <button @click="clk_0" type="button" class="btn btn-outline-primary sele">小学</button>
						  </div>
						  <div class="p-2">
							  <button @click="clk_1" type="button" class="btn btn-outline-primary sele">初中</button>
						  </div>
						  <div class="p-2">
							  <button @click="clk_2" type="button" class="btn btn-outline-primary sele">高中</button>
						  </div>
						  <div class="p-2">
							<button @click="clk_3" type="button" class="btn btn-outline-primary sele">大学</button>
						  </div>
						</div>
						<div class="d-flex flex-row mb-3">
						  <div class="p-2">
							  <button @click="clk_4" type="button" class="btn btn-outline-primary sele">四级</button>
						  </div>
						  <div class="p-2">
							  <button @click="clk_5" type="button" class="btn btn-outline-primary sele">六级</button>
						  </div>
						  <div class="p-2">
							  <button @click="clk_6" type="button" class="btn btn-outline-primary sele">雅思</button>
						  </div>
						</div>
						
                        <div class="d-flex flex-column mb-3" style="align-items: center;">
                            

                        </div>
                    </div>
                </div>
                <div class="card col-12">
                    <div class="card-body">
                        <div v-for="audio in audios" v-bind:key="audio.resourceName" class="card resource" style="margin-top: 10px;">
                            <div class="card-body">
                                <div class="row">
                                    <div class="col">
                                        <p>{{ audio.resourceName }}</p>
                                    </div>
                                    <div class="col">
                                        <!-- <a download href="http://81.70.183.49:8000/static/videos/%E6%89%AC%E5%B7%9E%E5%B0%8F%E5%AD%A6%E5%85%AD%E5%B9%B4%E7%BA%A7%E4%B8%8A%E5%86%8C%E6%9C%9F%E6%9C%AB.wav">下载</a> -->
                                        <button @click="download(audio)" type="button" class="btn btn-primary opt">保存音频</button>
                                        
                                        <button @click="golisten(audio)" type="button" class="btn btn-primary opt">前往练习</button>
                                    </div>
                                </div>
                            </div>
                        </div>
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
    name: "PastPapersView",
    components: {
        ContentBase,
    },

    setup() {
        let store = useStore();
        let audios = ref([]);
        let router = useRouter();

        // 接口，获取用户的所有保存收藏的音频
        // $.ajax({
        //     url: "http://81.70.183.49:8000/vueApi/getforeignlisten",
        //     type: "get",
        //     success(resp) {
        //         let getvideos = resp.videos;
        //         videos.value = getvideos;
        //         console.log(videos.value);
        //     }
        // });

        // 把需要的听力资源存到vuex中
        const golisten = (video) => {
            store.commit("changeListen", video);
            router.replace({ name: "player" });
        };

        // TODO 接口

        const pastPapers = (type) => {
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/getpastpapers/",
                type: "get",
                data: {
                    'suitable': type,
                },
                success(resp) {
                    audios.value = resp.past_papers;
                    console.log(audios.value);
                }
            });
        }

        // 小学听力
        const clk_0 = () => {
            // audios.value = [];
            pastPapers('primary school');
        };

        // 初中听力
        const clk_1 = () => {
            pastPapers('junior high');
        }; 

        // 高中听力
        const clk_2 = () => {
            pastPapers('high school');
        };

        // 大学听力
        const clk_3 = () => {
            pastPapers('college');
        };

        // 四级听力
        const clk_4 = () => {
            pastPapers('cet 4');
        };

        // 六级听力
        const clk_5 = () => {
            pastPapers('cet 6');
        };

        // 雅思听力
        const clk_6 = () => {
            pastPapers('IELTS');
        };

        // 使用XmlHttpRequest来请求后端api，使用jquery的ajax则会导致blob数据无法被辨认
        const download = (audio) => {
            const url = 'http://81.70.183.49:8000/vueApi/download/' + audio.resourceUrl; // 替换为你的后端 URL
    
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
            audios,
            golisten,
            clk_0,
            clk_1,
            clk_2,
            clk_3,
            clk_4,
            clk_5,
            clk_6,
            download,
        }
    }
}
</script>

<style scoped>
button {
    width: 60%;
    height: 40px;
    margin-top: 20px;
    margin-bottom: 20px;
}


.resource {
    user-select: none;
    cursor: pointer; 
    -webkit-transition: all .5s; 
    -moz-transition: all .5s; 
    -ms-transition: all .5s; 
    -o-transition: all .5s; 
    transition: all .5s;
    background-color: white;
}
.resource:hover {
    background-color: #F6F7F5;
}
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

.sele {
	width: 40px;
	height: 60px;
}

.opt {
	width: 100px;
	height: 40px;
}
</style>