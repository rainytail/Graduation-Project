<template>
    <ContentBase>
        <div class="container text-center">
            <div class="row">
                <div class="col">
                    <img style="width: 100%" :src="imgSrc" alt="">
                </div>
                <div class="col">
                    <transition name="fade" mode="out-in">
                        <p class="name" @click="click_router">{{ username }}</p>
                    </transition>
                </div>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from './ContentBase.vue';
import { ref, reactive } from 'vue';
import router from '@/router/index';

export default {
    name: "UserCard",
    props: {
        share: {
            type: Object,
            required: true,
        }
    },
    components: {
        ContentBase,
    },
    setup(props) {
        let imgSrc = ref(props.share.avatar);
        let share = reactive(props.share);
        let userId = share.userId;
        let username = share.username;
        let content = share.content;

        const click_router = () => {
            router.replace({ name: 'userprofile', params: { userId: userId } });
        };

        return {
            imgSrc,
            username,
            userId,
            content,
            click_router,
        }
    }
}

</script>

<style scoped>
.name {
    font-size: 20px;
    user-select: none;
    cursor: pointer; 
    -webkit-transition: all .5s; 
    -moz-transition: all .5s; 
    -ms-transition: all .5s; 
    -o-transition: all .5s; 
    transition: all .5s;
}
.name:hover {
    font-size: 30px;
    color: cadetblue;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
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