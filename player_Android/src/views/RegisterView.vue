<template>
    <ContentBase>
        <div class="register">
            <p style="position: absolute;">Sign up</p>
        </div>
        <br /><br />
        <div class="row justify-content-md-center">
            <div class="col-12">
                <!-- 组织form submit的行为，并定义为函数register -->
                <form @submit.prevent="register">
                    <div class="mb-3">
                        <label for="register_username" class="form-label">Username</label>
                        <input v-model="username" type="text" class="form-control" id="register_username" aria-describedby="emailHelp">
                        <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                    </div>
                    <div class="mb-3">
                        <label for="register_password" class="form-label">Password</label>
                        <input v-model="password" type="password" class="form-control" id="register_password">
                    </div>
                    <div class="mb-3">
                        <label for="register_password" class="form-label">Age</label>
                        <input v-model="age" type="number" class="form-control" id="register_password">
                    </div>
                    <div class="mb-3">
                        <label for="register_password" class="form-label">目前规划</label>
                        <!-- <input v-model="password" type="password" class="form-control" id="register_password"> -->
                        <select v-model="want" class="form-select" aria-label="Default select example">
                            <option selected value="-1">点击选择规划</option>
                            <option value="0">初中</option>
                            <option value="1">高中</option>
                            <option value="2">大学</option>
                            <option value="3">四级</option>
                            <option value="4">六级</option>
                            <option value="5">雅思</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="avatar" class="form-label">Avatar</label>
                        <input v-model="avatar" type="text" class="form-control" id="avatar">
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
import router from '@/router/index';
import $ from 'jquery';
import { useStore } from 'vuex';

export default {
    name: 'RegisterView',
    components: {
        ContentBase,
    },

    setup() {
        let username = ref('');
        let password = ref('');
        let age = ref('');
        let want = ref('-1');
        let error_message = ref('');
        let avatar = ref('http://81.70.183.49:8000/static/images/1.jpg');

        let store = useStore();
        


        const register = () => {
            error_message.value = "";
            console.log(username.value, password.value);
            // 使用dispatch调用action, 调用的是action中的login函数
            if (want.value == '-1') {
                alert('请选择目前学习方向!');
                return ;
            }
            let to_learn = '';
            if (want.value == 0) to_learn = 'primary school';
            else if (want.value == 1) to_learn = 'high school';
            else if (want.value == 2) to_learn = 'college';
            else if (want.value == 3) to_learn = 'cet 4';
            else if (want.value == 4) to_learn = 'cet 5';
            else if (want.value == 5) to_learn = 'IELTS';
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/register/",
                type: "get",
                data: {
                    "username": username.value,
                    "password": password.value,
                    "userage": age.value,
                    "user_urge": to_learn,
                    "avatar": avatar.value,
                },
                success(resp) {
                    if (resp.result === "success") {
                        error_message.value = "注册成功，即将跳转";
                        store.dispatch("sleep", 2000);
                        // push函数是在当前url上增加新的/login，因此会变成 /register/login，需要换成replace并且使用name的形式
                        router.replace({name: "login"});
                    } else {
                        error_message.value = resp.error_message;
                    }
                }
            })
        }

        return {
            username,
            password,
            error_message,
            age,
            want,
            register,
        }
    }
}
</script>

<style scoped>
.container {
    margin-top: 20px;
}
.register {
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