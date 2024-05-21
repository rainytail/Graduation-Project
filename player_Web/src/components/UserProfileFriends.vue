<template>
    <ContentBase>
        <div v-for="friend in friends" :key="friend.userId" style="margin-bottom: 20px;" class="card" @click="to_friend(friend)">
            <div class="card-body">
                <div class="container text-center">
                    <div class="row">
                        <div class="col-4">
                            <div class="card-avatar" :style="{ backgroundImage: 'url(' + friend.avatar + ')' }"></div>
                        </div>
                        <div class="col-8">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col">
                                        <div class="card-title">{{ friend.username }}</div>
                                        <div class="card-subtitle">{{ friend.userlabel }}</div>
                                    </div>
                                    <div class="col">
                                        <div class="card-title2">年龄: {{ friend.userage }}</div>
                                        <div class="card-title2">目前学习: {{ friend.user_urge }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <br>
        </div>
    </ContentBase>
</template>


<script>
import ContentBase from './ContentBase.vue';
import axios from 'axios';
import { useStore } from 'vuex';
import { ref, onMounted } from 'vue';
import router from '@/router/index';

export default {
    name: 'UserProfileFriends',
    components: {
        ContentBase,
    },
    setup() {
        const store = useStore();
        const friends = ref([]);

        const fetchFriends = async () => {
            try {
                const friendsResponse = await axios.get("http://81.70.183.49:8000/vueApi/get_friends/", {
                    params: {
                        userId: store.state.user.id,
                    }
                });
                const friendPromises = friendsResponse.data.friends.map(friendInfo =>
                    axios.get("http://81.70.183.49:8000/vueApi/get_friend_info", {
                        params: { userId: friendInfo.friendId }
                    })
                );

                const friendDetailsResponses = await Promise.all(friendPromises);
                friends.value = friendDetailsResponses.map(res => res.data.friend);
            } catch (error) {
                console.error("Failed to fetch friends:", error);
            }
        };


        onMounted(() => {
            fetchFriends();
        });

        const to_friend = (friend) => {
            console.log(friend);
            // 强制重新加载当前页面
            router.replace({ name: 'home' }).then(() => {
                router.replace({ name: 'userprofile', params: { userId: friend.userId } });
            });
        };


        return {
            friends,
            to_friend,
        };
    }
}
</script>

<style scoped>
.card {
    user-select: none;
    cursor: pointer; 
    transition: all .5s;
    background-color: white;
}
.card:hover {
    background-color: #F6F7F5;
}

.card-info {
 display: flex;
 flex-direction: column;
 justify-content: center;
 align-items: center;
 transition: transform .2s ease, opacity .2s ease;
}

/*Image*/
.card-avatar {
 --size: 60px;
 background: linear-gradient(to top, #f1e1c1 0%, #fcbc97 100%);
 width: var(--size);
 height: var(--size);
 border-radius: 50%;
 background-size: 100% 100%;
 transition: transform .2s ease;
 margin-bottom: 1rem;
}


/*Card footer*/
.card-social {
 transform: translateY(200%);
 display: flex;
 justify-content: space-around;
 width: 100%;
 opacity: 0;
 transition: transform .2s ease, opacity .2s ease;
}

.card-social__item {
 list-style: none;
}

.card-social__item svg {
 display: block;
 height: 18px;
 width: 18px;
 fill: #515F65;
 cursor: pointer;
 transition: fill 0.2s ease ,transform 0.2s ease;
}

/*Text*/
.card-title {
 color: #333;
 font-size: 1.5em;
 font-weight: 600;
 line-height: 2rem;
}

.card-title2 {
 color: #333;
 font-size: 1.1em;
 font-weight: 400;
 line-height: 1.7rem;
}

.card-others {
 color: #333;
 font-size: 1em;
 font-weight: 600;
 line-height: 2rem;
}

.card-subtitle {
 color: #859ba8;
 font-size: 0.8em;
}

/*Hover*/
.card:hover {
 box-shadow: 0 8px 50px #23232333;
}

.card:hover .card-info {
 transform: translateY(-5%);
}

.card:hover .card-social {
 transform: translateY(100%);
 opacity: 1;
}

.card-social__item svg:hover {
 fill: #232323;
 transform: scale(1.1);
}

.card-avatar:hover {
 transform: scale(1.1);
}
</style>