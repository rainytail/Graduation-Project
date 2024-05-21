<template>
  <!-- // router-view 按具体链接渲染 -->
  <!-- <div class="container text-center">
    <div class="row">
      <div class="col-3" style="height: 100%">
        <UserTool></UserTool>
      </div>
      <div class="col-9" style="height: 100%">
        <NeighborhoodView></NeighborhoodView>
      </div>
    </div>
  </div> -->
  <ContentBase></ContentBase>
</template>
  
  // 首页
  
<script>
// @ is an alias to /src
// import UserTool from '../components/UserTool.vue'
// import NeighborhoodView from './NeighborhoodView.vue'
import axios from 'axios'
// import { ref } from 'vue'

import ContentBase from '@/components/ContentBase.vue'

export default {
  name: 'HomeView',
  components: {
    // UserTool,
    // NeighborhoodView,
    ContentBase,
  },
  setup() {
    axios({
      url: "http://81.70.183.49:8000/vueApi/hello_world"  //如果不指定method，默认发送get请求
    }).then(res => {
      console.log(res)
    })
  }
}
</script>

<style scoped>
.container {
  margin-top: 20px;
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
  