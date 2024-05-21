<!-- 头像和基础信息 -->
<template>
    <div class="card" style="width: 18rem; display: flex; justify-content: center;/*水平主轴居中*/">
        <img style="width: 80%; position: relative; left: 25px; top: 10px" :src="avatar" class="card-img-top" alt="user">
        <div class="card-body">
            <h5 class="card-title">{{ _user.username }}</h5>
            <p class="card-text">{{ _user.userlabel }}</p>
            <!-- <p class="card-text">关注数量：{{ $store.state.user.followersCount }}</p> -->
            <!-- 使用v-if来动态渲染，使用@click=""来绑定函数 -->
            <button v-if="user.userId != $store.state.user.id && not_friend" @click="change" type="button" class="btn btn-outline-secondary">关注</button>
            <button v-if="user.userId != $store.state.user.id && !not_friend" @click="change" type="button" class="btn btn-outline-secondary">取消关注</button>
            <button v-if="user.userId == $store.state.user.id" @click="showfriends" type="button" class="btn btn-outline-secondary">我的好友</button>
            <button v-if="user.userId == $store.state.user.id" @click="showSettings" type="button" class="btn btn-outline-secondary">设置</button>
            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
        </div>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { ref, reactive } from 'vue';
import $ from 'jquery';

export default {
    name: "UserProfileL",

    // props可以定义需要从父组件中获取到的数据
    props: {
        user: {
            type: Object,
            required: true
        },
    },

    // 如果需要从props中计算其他数据，需要使用computed来计算
    // context API，使用context的emit函数可以触发父组件中使用@定义的触发函数
    setup(props, context) {
        console.log("L 部分传递下来的user: ", props.user);
        let _user = reactive(props.user);

        let store = useStore();
        console.log("avatar: ", store.state.user);
        let avatar = ref(_user.avatar);

        console.log(props.user.userId, store.state.user.id);

        let fullname = computed(() => props.user.lastname + ' ' + props.user.firstname);
        fullname = computed(()=>props.user.username);

        let not_friend = ref(false);
        $.ajax({
            url: "http://81.70.183.49:8000/vueApi/is_friend",
            type: "get",
            data: {
                "meId": String(store.state.user.id),
                "youId": String(_user.userId),
            },
            success(resp) {
                if (resp.answer == 'false') {
                    not_friend.value = true;
                } else {
                    not_friend.value = false;
                }
            }
        });



        const follow = () => {
            console.log("follow");
            context.emit('follow');
        };

        const unfollow = () => {
            console.log("unfollow");
            context.emit('unfollow');
        };

        const showfriends = () => {
            context.emit('showfriends');
        };

        const showSettings = () => {
            context.emit('showSettings');
        }

        console.log("meid youid : ", String(store.state.user.id),  String(_user.userId));

        const change = () => {
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/change_relationship",
                type: "get",
                data: {
                    "meId": String(store.state.user.id),
                    "youId": String(_user.userId),
                },
                success() {
                    not_friend.value = !(not_friend.value);
                }
            });
        };

        return {
            fullname,
            follow,
            unfollow,
            avatar,
            _user,
            showfriends,
            change,
            not_friend,
            showSettings,
        }
    }
}
</script>

<style scoped>
img {
    border-radius: 50%;
}

button {
    margin-right: 10px;
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