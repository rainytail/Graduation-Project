<template>
    <ContentBase>
        <!-- <div class="row"> -->
            <!-- <div class="col-3"> -->
                <!-- 使用:user的形式把user传递给子组件 -->
                <UserProfileL @showfriends="showfriends" @follow="follow" @unfollow="unfollow" :user="user"></UserProfileL>
                <!-- <UserProfileWrite @post_a_post="post_a_post"></UserProfileWrite> -->
            <!-- </div> -->
            <!-- <div class="col-9"> -->
                <UserProfileR v-if="now_display==='settings'"></UserProfileR>
                <UserProfileRPosts v-if="now_display==='posts'" :posts="posts"></UserProfileRPosts>
                <UserProfileFriends v-if="now_display==='friends'"></UserProfileFriends>
            <!-- </div> -->
        <!-- </div> -->
    </ContentBase>
</template>

<script>
import { reactive } from 'vue';
import ContentBase from '../components/ContentBase.vue';
import UserProfileL from '../components/UserProfileL.vue'
import UserProfileR from '../components/UserProfileR.vue'
import UserProfileRPosts from '../components/UserProfileRPosts.vue'
import UserProfileWrite from '../components/UserPostWrite.vue'
import UserProfileFriends from '../components/UserProfileFriends.vue'

// useroute可以获取url的参数
import { useRoute } from 'vue-router';
import $ from 'jquery';
import { ref } from 'vue';

export default {
    name: 'UserProfileView',
    components: {
        ContentBase,
        UserProfileL,
        UserProfileR,
        UserProfileRPosts,
        UserProfileWrite,
        UserProfileFriends
    },
    // setup 函数用来初始化变量
    setup() {
        // 获取route
        const route = useRoute();
        // 获取route中的参数
        console.log("抓取到参数userId: ", route.params.userId);

        let now_display = ref("posts");


        // reactive初始化一个对象
        let user = reactive({
            userId: 1,
            username: "rainytail",
            lastname: "rain",
            firstname: "tail",
            followersCount: 0,
            is_followed: false,
            userlabel: "好好学习，天天向上",
            now_display: "posts",
        });

        $.ajax({
            url: "http://81.70.183.49:8000/vueApi/getUser",
            data: {
                'userId': String(route.params.userId),
            },
            async: false,
            type: "get",
            success(resp) {
                user = resp.user;
                console.log("userId: ", String(route.params.userId), " user: ", user);
            }
        });

        let posts = reactive({
            // count: 3,
            // posts: [
            //     {
            //         id: 1,
            //         userId: 1,
            //         content: "1",
            //     },
            //     {
            //         id: 2,
            //         userId: 1,
            //         content: "2",
            //     },
            //     {
            //         id: 3,
            //         userId: 1,
            //         content: "3",
            //     },
            // ]
        });

        $.ajax({
            url: "http://81.70.183.49:8000/vueApi/get_share_posts/",
            type: 'get',
            data: {
                'userId': String(route.params.userId),
            },
            async: false,
            success(resp) {
                posts = resp.posts;
                console.log(posts);
            }
        });

        const follow = () => {
            if (user.is_followed) return ;
            user.is_followed = true;
            user.followersCount ++ ;
        };

        const unfollow = () => {
            if (user.is_followed === false) return ;
            user.is_followed = false;
            user.followersCount -- ;
        };

        const post_a_post = (content) => {
            posts.count ++ ;
            posts.posts.unshift({
                id: posts.count,
                userId: 1,
                content: content,
            });
        };

        const showfriends = () => {
            now_display.value = "friends";
        }

        // return出去给别的组件使用
        return {
            user: user,
            follow,
            unfollow,
            posts,
            post_a_post,
            now_display,
            showfriends,
        }
    },
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