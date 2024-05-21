// import axios from 'axios'
// import $ from 'jquery'
// import qs from 'qs'
// import { jwtDecode } from 'jwt-decode';
// import $ from 'jquery';

// import router from '@/router/index';

const ModuleListen = {
    state: {
        listen: {
            listen_type: "local",
            now_listen: null,
        }
    }, // 存数据
    getters: {}, // 通过计算得到的数据，需要通过getter获取，类似于compute
    mutations: {
        changeListen(state, video) {
            state.now_listen = video;
            state.listen_type = video.type;
        },

    }, // 定义对数据的操作（修改）
    actions: {

    },
    modules: {}
};

export default ModuleListen;