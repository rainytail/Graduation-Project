<template>
    <div class="card">
        <div class="card-body" style="width: 100%;">
            <h5 id="title" class="card-title">111</h5>
            <audio preload="auto" controls id="player" ref="player" class="aud">
                <source :src="audioUrl" />
            </audio>
            <!-- <div class="selece-audio">
                实现选择文件
                定义一个隐藏的文件选择器
                <input ref="fileInput" type="file" style="display: none" @change="handleFileChange">
                点击按钮触发文件选择器
                <button @click="openFilePicker" type="button" class="btn btn-outline-secondary">选择音频</button>
                只有在selectFile.value存在时才渲染，避免select
                <label id="filename" v-if="not_display" style="margin-left: 20px;" for=""></label>
                <button @click="chooseAudio" style="float:right" type="button" class="btn btn-outline-secondary">确认</button>
            </div> -->
            <div class="d-flex justify-content-around">
                <button @click="back5" type="button" class="btn btn-outline-secondary">后退五秒</button>
                <button @click="forward5" type="button" class="btn btn-outline-secondary">前进五秒</button>
                <button @click="parse" type="button" class="btn btn-outline-secondary">暂停/播放</button>
                <select v-model="selectOption" @click="test" @change="handleChange" style="width:auto" class="form-select" aria-label="Default select example">
                    <option selected value="0">原速</option>
                    <option value="1">1.25倍速</option>
                    <option value="2">1.5倍速</option>
                    <option value="3">0.75倍速</option>
                    <option value="4">0.5倍速</option>
                </select>
            </div>
            <!-- 控制速度 -->
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    name: "DailyPlayer",
    props: {
        daily_audio: {
            type: Object,
            required: true,
        }
    },
    setup(props) {
        // setup函数在vue组件渲染之前就先执行，这时候dom树中的元素还不存在，因此需要使用ref函数将变量与元素绑定，从而获取到
        // 对应元素。获取方式：在元素中加入 ref="xx" 其中xx是变量名字
        let player = ref(null);

        console.log("daily_audio: ", props.daily_audio);

        let selectOption = ref("0");

        let fileInput = ref(null);

        let selectedFile = ref('');
        let not_display = ref(true);
        
        let audioUrl = ref('http://81.70.183.49:8000/static/videos/' + props.daily_audio.resourceUrl);

        // console.log("1111", audioUrl.value)

        // 在组件挂载后执行的逻辑
        onMounted(() => {
            const title = document.querySelector('#title');
            if (title) {
                title.textContent = props.daily_audio.resourceName;
                console.log("playerUrl: ", audioUrl.value);
                // 调用audio的load事件来更新音频文件
                player.value.load();
            } else console.log("chooseAudio failed");
        });


        const parse = () => {
            if (player.value.paused) {
                player.value.play();
            } else {
                player.value.pause();
            }
        };

        const back5 = () => {
            console.log("back 5", player.value.currentTime);
            player.value.currentTime -= 5;
            if (player.value.currentTime < 0) {
                player.value.currentTime = 0;
            }
        };

        const forward5 = () => {
            console.log("forward 5", player.value.currentTime);
            player.value.currentTime += 5;
            if (player.value.currentTime > player.value.duration) {
                player.value.currentTime = player.value.duration;
                player.value.pause();
            }
        };

        // 修改倍速后，需要进行pause()和play()才能正常改变倍速
        const handleChange = () => {
            console.log("now handleChange", player.value.playbackRate);
            switch(selectOption.value) {
                case "0":
                    player.value.playbackRate = parseFloat(1);
                    player.value.pause();
                    player.value.play();
                    break;
                case "1":
                    player.value.playbackRate = parseFloat(1.25);
                    player.value.pause();
                    player.value.play();
                    console.log("change player rate 1.25");
                    break;
                case "2":
                    player.value.playbackRate = parseFloat(1.5);
                    player.value.pause();
                    player.value.play();
                    break;
                case "3":
                    player.value.playbackRate = 0.75;
                    player.value.pause();
                    player.value.play();
                    break;
                case "4":
                    player.value.playbackRate = 0.5;
                    player.value.pause();
                    player.value.play();
                    break;
                default:
                    console.log("others");
            }
            // player.value.load();
        };

        const test = () => {
            console.log(selectOption.value);
        };
        
        // 打开文件选择器的方法
        const openFilePicker = () => {
            // 触发文件选择器点击事件
            fileInput.value.click();
        };
        // 文件选择变化时触发的方法
        const handleFileChange = (event) => {
            not_display.value = true;
            // 获取选择的文件对象
            selectedFile.value = event.target.files[0];
            // 这里可以对选择的文件进行处理，例如上传等操作
            console.log('Selected file:', selectedFile);
            const fileNameLabel = document.querySelector('#filename');
            if (fileNameLabel) {
                fileNameLabel.textContent = selectedFile.value.name;
            }
        };

        const chooseAudio = () => {
            const title = document.querySelector('#title');
            if (title) {
                title.textContent = selectedFile.value.name;
                audioUrl.value = '/audios/' + selectedFile.value.name + "?" + Date.now();
                console.log("playerUrl: ", audioUrl.value);
                // 调用audio的load事件来更新音频文件
                player.value.load();
            } else console.log("chooseAudio failed");
        }

        return {
            selectOption,
            player,
            parse,
            back5,
            forward5,
            handleChange,
            test,
            openFilePicker,
            handleFileChange,
            fileInput,
            selectedFile,
            not_display,
            chooseAudio,
            audioUrl,
        }
    },
};



</script>

<style scoped>
audio {
  width: 100%;
  max-width: 700px;
  margin: 0 auto;
}
.selece-audio {
    /* margin: 20px; */
    padding: 10px;
}
* {
    margin: 8px;
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