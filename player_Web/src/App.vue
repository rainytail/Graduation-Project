<template>
  <div id="app">
    <NavBar></NavBar>
    <!-- // router-view 按具体链接渲染 -->
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import { useStore } from 'vuex';

export default {
  name: "App",
  // 需要使用到的组件
  components: {
    NavBar,
  },
  setup() {
    let store = useStore();
    
    console.log(store.state.user);

    // store.commit("updateUser", {
    //   userId: '6',
    //   username: "123",
    //   password: "123",
    //   firstname: "",
    //   lastname: "",
    //   userlabel: "好好学习",
    //   followersCount: 0,
    //   avatar: "http://81.70.183.49:8000/static/images/1.jpg", // 头像
    //   is_login: true,
    //   now_listen: null,
    //   listen_type: "cloud",
    //   userage: '12',
    //   user_urge: 'primary school',
    // })
  }
}
</script>

<style>

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

#app {
  background-image: url('/public/images/bg.jpg');
  background-size: cover;
  background-position: center;
  min-height: 100vh;  /* 使得背景至少覆盖整个视口 */
}

</style>
