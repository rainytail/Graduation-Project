<template>
    <div class="card">
        <div class="card-body" style="width: 100%;">
            <button @click="toText" type="button" class="btn btn-outline-secondary">显示听力文本</button>
            <pre v-if="show" id="formattedText">{{ content }}</pre>
            <p v-else>content</p>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import $ from 'jquery';
// import { useStore } from 'vuex';

export default {
    name: "TextContent",
    props: {
        file: {
            type: Object,
        },
    },
    setup(props) {
        // let store = useStore();

        let content = ref('');
        let show = ref(true);

        // const fetchData = () => {
        //     $.ajax({
        //         url: "http://81.70.183.49:8000/vueApi/gettext/",
        //         type: "get",
        //         data: {
        //             "videoUrl": "1.mp3",
        //         },
        //         success(resp) {
        //             content.value = resp.text;
        //         },
        //         error(error) {
        //             console.error("Ajax 请求失败:", error);
        //         }
        //     });
        // };

        const audio2Base64 = () => {
            // var file = 'audios/' + store.state.user.now_listen.name;
            console.log("audio2Base64: ", props.file.value);
            const reader = new FileReader()
            reader.readAsDataURL(props.file.value);
            reader.onload = function () {
                const base64String = reader.result.split(",")[1];
                console.log(base64String);
            };
        }

        const toText = () => {
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/video2text/",
                type: 'get',
                data: {
                    'file': props.file.name,
                    
                },
                success(resp) {
                    let preformattedText = document.getElementById('formattedText');

                    let text = resp.text.result[0];
                    let sentences = '';

                    for (let i = 0, sentence = ''; i < text.length; i ++ ) {
                        sentence += text[i];
                        if (text[i] == '.' || text[i] == '?' || text[i] == '!') {
                            if (sentence.length != 0 && sentence[0] == ' ') {
                                sentence = sentence.slice(1, sentence.length);
                            }
                            sentences += sentence + '\n';
                            sentence = '';
                        }
                    }
                    let str = sentences.replace(/\n/g, "<br>");
                    preformattedText.innerHTML = str;
                },
            })
        }

        const clk = () => {
            show.value = !show.value;
        };

        onMounted(() => {
            console.log("组件挂载完成，调用 Ajax 请求");
            // fetchData();
            // toText();
        });

        return {
            content,
            show,
            clk,
            audio2Base64,
            toText,
        }
    }
}
</script>

<style scoped>
blockquote {
    text-align: left;
    font-size: 1.25rem;
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