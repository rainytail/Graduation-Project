<!-- 设置 -->
<template>
    <div class="container">
        <div class="card">
            <div class="register">
                <p style="float: left">Settings</p>
            </div>
            <blockquote></blockquote>
            <div class="row justify-content-md-center">
                <div class="col-6">
                    <!-- 组织form submit的行为，并定义为函数register -->
                    <form @submit.prevent="change">
                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">Username</span>
                            <input v-model="username" type="text" class="form-control" :placeholder="user.username" aria-label="Username" aria-describedby="basic-addon1">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">Password</span>
                            <input type="password" v-model="password" class="form-control" placeholder="Password" id="register_password" aria-label="Username" aria-describedby="basic-addon1">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">Age</span>
                            <input type="number" v-model="age" class="form-control" :placeholder="user.age" id="register_password" aria-label="Username" aria-describedby="basic-addon1">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">目前规划</span>
                            <select v-model="want" class="form-select" aria-label="Default select example">
                                <option selected value="-1">{{ learning }}</option>
                                <option value="0">初中</option>
                                <option value="1">高中</option>
                                <option value="2">大学</option>
                                <option value="3">四级</option>
                                <option value="4">六级</option>
                                <option value="5">雅思</option>
                            </select>
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text" id="basic-addon1">Avatar</span>
                            <input v-model="avatar" type="text" :placeholder="user.avatar" class="form-control" id="avatar">
                        </div>

                        <div class="input-group">
                            <span class="input-group-text">签名</span>
                            <textarea id="textarea" :placeholder="user.label" class="form-control" aria-label="With textarea"></textarea>
                        </div>

                        <div class="error-message">{{ error_message }}</div>
                        <button style="width: 100%;" type="submit" class="btn btn-primary">修改</button>
                    </form>
                </div>
            </div>
        </div>
    </div>  
</template>

<script>
import ContentBase from './ContentBase.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import $ from 'jquery';
import router from '@/router/index';

export default {
    name: "UserProfileSettings",
    components: ContentBase,
    setup() {
        let username = ref('');
        let password = ref('');
        let age = ref('');
        let want = ref('-1');
        let error_message = ref('');
        let avatar = ref('http://81.70.183.49:8000/static/images/1.jpg');

        let store = useStore();

        let user = store.state.user;
        console.log(user);
        let learning = ref('');
        if (user.urge == -1) learning.value = "小学";
        else if (user.urge == 0) learning.value = "初中";
        else if (user.urge == 1) learning.value = "高中";
        else if (user.urge == 2) learning.value = "大学";
        else if (user.urge == 3) learning.value = "四级考";
        else if (user.urge == 4) learning.value = "六级考";
        else if (user.urge == 5) learning.value = '雅思';
        else learning.value = '其他';

        console.log("learning: ", learning.value);

        


        const change = () => {
            error_message.value = "";
            console.log(username.value, password.value);
            // 使用dispatch调用action, 调用的是action中的login函数
            let to_learn = '';
            if (want.value == '-1') to_learn = 'primary school';
            else if (want.value == 0) to_learn = 'junior high';
            else if (want.value == 1) to_learn = 'high school';
            else if (want.value == 2) to_learn = 'college';
            else if (want.value == 3) to_learn = 'cet 4';
            else if (want.value == 4) to_learn = 'cet 5';
            else if (want.value == 5) to_learn = 'IELTS';

            
            console.log("age urge: ", age.value, want.value);

            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/change_user/",
                type: "get",
                data: {
                    "userId": store.state.user.id,
                    "username": username.value,
                    "password": password.value,
                    "userage": String(age.value),
                    "user_urge": to_learn,
                    "avatar": avatar.value,
                    "userlabel": document.getElementById('textarea').value,
                },
                success(resp) {
                    if (resp.result === "success") {
                        error_message.value = "注册成功，即将跳转";
                        store.dispatch("sleep", 2000);
                        // push函数是在当前url上增加新的/login，因此会变成 /register/login，需要换成replace并且使用name的形式
                        alert("修改成功!");
                        store.dispatch("login", {
                            username: username.value == '' ? store.state.user.username : username.value,
                            password: password.value == '' ? store.state.user.password : password.value,
                            success(resp) {
                                router.push({ name: 'userprofile', params: { userId: resp } });
                            },
                            error() {
                                console.log(username.value, password.value);
                                error_message.value = "用户名或密码错误";
                                console.log(error_message.value);
                            },
                        })
                        console.log("change user: ", store.state.user);
                        router.replace({ name: 'home' }).then(() => {
                            router.replace({ name: 'userprofile', params: { userId: user.id } });
                        });
                    } else {
                        error_message.value = resp.error_message;
                    }
                }
            })
        }

        return {
            change,
            learning,
            error_message,
            user,
            age,
            want,
            username,
            password,
            avatar,
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
.register {
    font-size: 2rem;
    line-height: 1.75rem;
    font-weight: 600;
    text-align: center;
    color: #000;
    float: left;
}
* {
    margin: 10px;
}
</style>