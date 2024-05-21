<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
        <!-- Vue Router 可以在不重新加载页面的情况下更改 URL -->
        <router-link class="title" :to="{name: 'home'}">English Player</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" style="margin-left: 20px;">
        <ul v-if="$store.state.user.is_login" class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <router-link class="nav-link" :to="{name: 'myvideos'}">音频保存</router-link>
            </li>
            <li class="nav-item">
                <transition name="fade" mode="out-in">
                    
                <router-link class="nav-link" :to="{name: 'player'}">听力练习</router-link>
                </transition>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    英文听力精读
                </a>
                <ul class="dropdown-menu">
                    <li>
                        <router-link class="nav-link dropdown-item" :to="{name: 'foreignListen'}">外刊听力</router-link>
                    </li>
                    <li>
                        <router-link class="nav-link dropdown-item" :to="{name: 'pastPapers'}">真题听力</router-link>
                    </li>
                    <li><hr class="dropdown-divider"></li>
                    <li>
                        <router-link class="nav-link dropdown-item" :to="{name: 'notebooks'}">听力笔记</router-link>
                    </li>
                    <li>
                        <router-link class="nav-link dropdown-item" :to="{name: 'qualityListen'}">精读记录</router-link>
                    </li>
                </ul>
            </li>
            <router-link class="nav-link" :to="{name: 'dailyListen'}">每日听力</router-link>
            <router-link class="nav-link" :to="{name: 'neighborhood'}">社区动态</router-link>
            <router-link class="nav-link" :to="{name: 'cloudfile'}">我的云盘</router-link>
        </ul>
        <ul style="position: absolute; right: 120px" v-if="!$store.state.user.is_login" class="navbar-nav me-auto mb-2">
            <li class="nav-item">
                <router-link class="nav-link" :to="{name: 'login'}">登录</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" :to="{name: 'register'}">注册</router-link>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="http://81.70.183.49:8000/admin">管理员登录</a>
            </li>
        </ul>
        <ul v-if="$store.state.user.is_login" class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <router-link class="nav-link" :to="{name: 'userprofile', params: {'userId': $store.state.user.id}}">
                    <p>{{ $store.state.user.username }}</p>
                </router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'home' }" @click="logout">退出</router-link>
            </li>
        </ul>
        </div>
    </div>
    </nav>
</template>

<script>
import { useStore } from 'vuex';
import router from '@/router/index';

export default {
   name: "NavBar", 
   setup() {
    let store = useStore();

    // console.log("navbar: ", store.state.user);
    // console.log("navbar login: ", store.state.user.is_login);
    // store.state.user.is_login = true;

    const logout = () => {
        console.log("执行routerlink 的click");
        store.dispatch('logout', {
            success() {
                router.push({ name: "home" });
            }
        });
    }

    return {
        logout,
    }
   }
}
</script>

<style scoped>
.title{
  text-shadow: 1px 1px black, -1px -1px black, 1px -1px black, -1px 1px black;
  font-size: 30px; 
  color:#fff;
  text-decoration: none;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}

nav {
    /* background-image: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%); */
    background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
}
</style>