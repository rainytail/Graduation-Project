<template>
    <ContentBase>
        <div class="login">
            <p style="position: absolute;">Sign in</p>
        </div>
        <br /><br />
        <div class="row justify-content-md-center">
            <div class="col-12">
                <!-- 组织form submit的行为，并定义为函数login -->
                <form @submit.prevent="login">
                    <div class="">
                        <label for="login_username" class="form-label">Username</label>
                        <input v-model="username" type="text" class="form-control" id="login_username" aria-describedby="emailHelp">
                        <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                    </div>
                    <div class="">
                        <label for="login_password" class="form-label">Password</label>
                        <input v-model="password" type="password" class="form-control" id="login_password">
                    </div>
                    <div class="error-message">{{ error_message }}</div>
                    <button style="width: 100%;" type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '../components/ContentBase.vue';
import { ref } from 'vue';
// 使用store全局数据
import { useStore } from 'vuex';
import router from '@/router/index';

export default {
    name: 'LoginView',
    components: {
        ContentBase,
    },

    setup() {
        let username = ref('');
        let password = ref('');
        let error_message = ref('');

        let store = useStore();

        const login = () => {
            error_message.value = "";
            console.log(username.value, password.value);
            // 使用dispatch调用action, 调用的是action中的login函数
            store.dispatch("login", {
                username: username.value,
                password: password.value,
                success(resp) {
                    router.push({ name: 'userprofile', params: { userId: resp } });
                },
                error() {
                    error_message.value = "用户名或密码错误";
                    console.log(error_message.value);
                },
            })
        }

        return {
            username,
            password,
            error_message,
            login,
        }
    }
}
</script>

<style scoped>
.container {
    /* margin-top: 20px; */
}
.login {
    font-size: 2rem;
    line-height: 1.75rem;
    font-weight: 600;
    text-align: center;
    color: #000;
    float: left;
}
.error-message {
    color: red;
    margin-bottom: 5px;
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