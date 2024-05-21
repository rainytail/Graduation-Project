import { createStore } from 'vuex'
import ModuleUser from './user'
import ModuleListen from './listen';

// vuex来维护全局变量
export default createStore({
    state: {}, // 存数据
    getters: {}, // 通过计算得到的数据，需要通过getter获取，类似于compute
    mutations: {}, // 定义对数据的操作（修改）
    actions: {
        sleep(delay) {
            let start = (new Date()).getTime();
            while ((new Date()).getTime() - start < delay) {
                continue;
            }
        },
    },
    // modules 用来把state进行对象分割
    modules: {
        user: ModuleUser,
        listen: ModuleListen,
    }
});

// store.state.user.username