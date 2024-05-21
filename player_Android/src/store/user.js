// import axios from 'axios'
import $ from 'jquery'
// import qs from 'qs'
// import { jwtDecode } from 'jwt-decode';
// import $ from 'jquery';

// import router from '@/router/index';

const ModuleUser = {
    state: {
        user: {
            id: '',
            username: "",
            firstname: "",
            lastname: "",
            label: "",
            age: "",
            urge: "",
            followersCount: 0,
            avatar: "", // 头像
            is_login: false,
            now_listen: null,
            listen_type: "cloud",
            now_display: "posts",
        },
    }, // 存数据
    getters: {
        fullName(state) {
            return state.user.firstname + state.user.lastname;
        }
    }, // 通过计算得到的数据，需要通过getter获取，类似于compute
    mutations: {

        updateUser(state, user) {
            state.id = user.userId;
            state.username = user.username;
            state.label = user.userlabel;
            state.avatar = user.avatar;
            state.age = user.userage;
            state.urge = user.user_urge;
            state.avatar = user.avatar;
            state.is_login = true;
            state.now_display = "posts";
            console.log("进行updateuser", state);
        },
        updateUser2(state, user) {
            state.id = user.id;
            state.username = user.username;
            state.label = user.label;
            state.avatar = user.avatar;
            state.age = user.age;
            state.urge = user.urge;
            state.avatar = user.avatar;
            state.is_login = true;
            state.now_display = "posts";
            console.log("进行updateuser", state);
        },
        logoutUser(state, user) {
            state.id = '';
            state.username = '';
            state.label = '';
            state.avatar = '';
            state.age = '';
            state.urge = '';
            state.is_login = false;
            user;
            console.log("进行logoutUser");
        }
    }, // 定义对数据的操作（修改）
    actions: {
        login(context, data) {
            // let param = new URLSearchParams();
            // param.append('username', data.username);
            // param.append('password', data.password);
            // axios({
            //     url: "http://81.70.183.49:8000/vueApi/login/", //如果不指定method，默认发送get请求
            //     method: "get",
            //     data: param,
            // }).then((resp) => {
            //     console.log(resp);
            //     console.log(data.username, data.password);
            // })

            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/login/",
                type: "get",
                data: {
                    username: data.username,
                    password: data.password,
                },
                success() {
                    // ajax获取用户信息
                    $.ajax({
                        url: "http://81.70.183.49:8000/vueApi/getinfo/",
                        type: "get",
                        data: {
                            username: data.username,
                        },
                        success(resp) {
                            context.commit("updateUser2", {
                                ...resp,
                                username: data.username,
                                password: data.password,
                            });
                            data.success(resp.id);

                        }
                    })

                    // console.log(resp);
                    // 成功之后调用data传下来的success函数
                    // data.success();
                },
                error() {
                    data.error();
                }
            })
        },

        logout(context, data) {
            console.log("执行vuex中的logout");
            context.commit("logoutUser", {});
            data.success();
        }
    },
    modules: {}
};

export default ModuleUser;