<template>
    <div class="card">
        <div class="card-body">
            <div class="container text-center">
                <div class="row">
                    <div class="col-7">  
                        <input v-model="to_translate_text" type="text" class="form-control" id="dictionary" placeholder="Search...">     
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="translator" value="0" checked>
                            <label class="form-check-label" for="flexRadioDefault1">
                                英->中
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="translator" value="1">
                            <label class="form-check-label" for="flexRadioDefault2">
                                中->英
                            </label>
                        </div>
                    </div>
                    <div class="col-3">
                        <button @click="translate" type="submit" class="btn btn-primary">查询</button>
                    </div>
                </div>
            </div>
            <textarea disabled v-model="translate_text" name="" id="" cols="60" rows="3">
                
            </textarea>

        </div>
    </div>
    
    <!-- <button @click="test">测试</button> -->
</template>

<script>
import $ from 'jquery';
import CryptoJS from 'crypto-js';
import { ref } from 'vue';

export default {
    name: "DictionaryComponent",
    setup() {
        let to_translate_text = ref('');
        let translate_text = ref('');
        let showMessage = ref(true);

        // let to_translate = "hello";
        function truncate(q){
            var len = q.length;
            if(len<=20) return q;
            return q.substring(0, 10) + len + q.substring(len-10, len);
        }

        const translate = () => {
            var appKey = '7164836ee6ba45d2';
            var key = 'mwmRFFRXUwles5o0cZLvPOijMf5x8C2F';
            var salt = (new Date).getTime();
            var curtime = Math.round(new Date().getTime()/1000);
            var query = to_translate_text.value;
            // 多个query可以用\n连接  如 query='apple\norange\nbanana\npear'
            var to = 'zh-CHS';
            var from = 'en';
            var str1 = appKey + truncate(query) + salt + curtime + key;
            // var vocabId =  '您的用户词表ID';
            //console.log('---',str1);
            var sign = CryptoJS.SHA256(str1).toString(CryptoJS.enc.Hex);

            // 翻译类型
            var scan = $("input[name='translator']:checked").val();
            if (scan == '0') {
                from = 'en';
                to = 'zh-CHS';
            } else {
                from = 'zh-CHS';
                to = 'en';
            }

            if (query == '') {
                showMessage.value = true;
                console.log("空，showmessage", showMessage.value);
                return ;
            } else showMessage.value = false;

            $.ajax({
                url: "https://openapi.youdao.com/api",
                type: "get",
                dataType: "jsonp",
                data: {
                    q: query,
                    appKey: appKey,
                    salt: salt,
                    from: from,
                    to: to,
                    sign: sign,
                    signType: "v3",
                    curtime: curtime,
                    // vocabId: vocabId,
                },
                success(resp) {
                    console.log(resp);
                    translate_text.value = resp.translation[0];
                }
            });
        };

        const test = () => {
            var scan = $("input[name='translator']:checked").val();
            console.log(scan);
        };

        return {
            translate,
            to_translate_text,
            translate_text,
            test,
        }
    }
}

</script>

<style scoped>
* {
    margin-top: 8px;
    margin-right: 10px;
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

textarea {
  resize: none;
  border: none;
  outline: none
}

/* 气泡框的样式 */
.tooltip {
  position: absolute;
  background-color: red;
  color: white;
  padding: 5px;
  border-radius: 5px;
  top: -30px; /* 控制气泡框位置 */
  left: 50%; /* 控制气泡框位置 */
  transform: translateX(-50%); /* 水平居中 */
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