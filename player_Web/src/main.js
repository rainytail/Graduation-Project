import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

// import qs from "qs"
// import Vue from 'vue'
import 'jquery'
import 'axios'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';

// Vue.pro
createApp(App).use(router).use(router).use(store).mount('#app')