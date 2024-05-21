<!-- 帖子动态 -->
<template>
    <div class="container">
        <ContentBase>
            <!-- 使用v-for来进行循环渲染，需要使用key值来绑定每一个循环对象 -->
            <!-- index是下标 -->
            <div v-for="post in posts" :key="post.id">
                <ShareContent style="width: 100%; height: 100%;" :share="post"></ShareContent>
                <!-- <div class="card single-post">
                    <div class="card-body">
                        {{ post.content }}
                    </div>
                </div> -->
            </div>
        </ContentBase>
    </div>  
</template>

<script>
import ContentBase from './ContentBase.vue';
import ShareContent from './ShareContent.vue';

export default {
    name: "UserProfileRPosts",
    components: {
        ContentBase,
        ShareContent,
    },
    props: {
        posts: {
            type: Object,
            required: true,
        },
    },
    setup(props) {
        console.log("传递下来的posts: " , props);
    }
}
</script>

<style scoped>
.single-post {
    margin-bottom: 10px;
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
</style>