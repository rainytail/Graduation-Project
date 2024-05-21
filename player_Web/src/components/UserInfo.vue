<template>
    <!-- <ContentBase> -->
        <div class="card">
            <div class="card-info">
                <div class="card-avatar" id="avatar"></div>
                <div class="card-title">{{ user.username }}</div>
                <div class="card-subtitle">{{ user.label }}</div>
            </div>
            <div class="container">
                <div class="card-others">年龄: {{ user.age }}</div>
                <!-- <br> -->
                <div class="card-others">目前学习: {{ learning }}</div>
            </div>
        </div>
    <!-- </ContentBase> -->
</template>

<script>
import { useStore } from 'vuex';
// import ContentBase from './ContentBase.vue';
import { onMounted, ref } from 'vue';



export default {
    name: "UserInfo",
    props: {
        share: {
            type: Object,
            required: false,
        }
    },
    components: {
        // ContentBase,
    },
    setup() {
        let store = useStore();
        let user = store.state.user;

        let learning = ref('');

        onMounted(() => {
            let url = user.avatar;
            document.getElementById('avatar').style.backgroundImage
                = 'url(' + url + ')'; 
            console.log("userinfo: urge: ", user.urge);
            if (user.urge == 'primary school') learning.value = "小学";
            else if (user.urge == 'junior high') learning.value = "初中";
            else if (user.urge == 'high school') learning.value = "高中";
            else if (user.urge == 'college') learning.value = "大学";
            else if (user.urge == 'cet 4') learning.value = "四级考";
            else if (user.urge == 'cet 6') learning.value = "六级考";
            else if (user.urge == 'IELTS') learning.value = '雅思';
            else learning.value = "其他";
        });
        
        return {
            user,
            learning,
        }
    }
}

</script>

<style scoped>
.card {
 width: 250px;
 height: 254px;
 background: #f5f5f5;
 padding: 2rem 1.5rem;
 transition: box-shadow .3s ease, transform .2s ease;
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