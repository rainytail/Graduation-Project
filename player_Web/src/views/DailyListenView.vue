<template>
    <ContentBase>
        <div class="container" v-if="!$store.state.user.id">
            <p>请先登录</p>
        </div>
        <div class="container" v-if="$store.state.user.id">
          <div class="container">
            <div class="row">
                <div class="col">
                  <DailyPlayer :daily_audio="daily_audio"></DailyPlayer>
                </div>
                <div class="col">
                    <DictionaryComponent></DictionaryComponent>
                    <PlayerText></PlayerText>
                </div>
            </div>
            <!-- <TextContent style="float: left; width: 50%;"></TextContent> -->
          </div>
        </div>
    </ContentBase>
</template>
  
<script>
// @ is an alias to /src
import ContentBase from '@/components/ContentBase.vue';
// import axios from 'axios'
import $ from 'jquery';
import DailyPlayer from '../components/DailyPlayer.vue';
// import { ref } from 'vue'
import { useStore } from 'vuex';
import { ref } from 'vue';
import PlayerText from '../components/PlayerContent.vue'
import DictionaryComponent from '../components/Dictionary.vue'

export default {
  name: 'DailyListenView',
  components: {
    ContentBase,
    DailyPlayer,
    PlayerText,
    DictionaryComponent,
  },
  setup() {
    let store = useStore();

    let daily_audio = ref(null);

    $.ajax({
      url: "http://81.70.183.49:8000/vueApi/dailyaudio",
      type: "get",
      data: {
        'date': Date.now(),
      },
      async: false,
      success(resp) {
        if (resp.result === "success") {
          console.log("dailyaudio接口调用成功", resp);
          daily_audio = resp.audio;
          console.log("向下传递: ", daily_audio);
          store.commit('changeListen', resp.audio);
        } else {
          console.log("dailyaudio接口调用失败");
        }
      }
    })

    return {
      daily_audio,
    }
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
  