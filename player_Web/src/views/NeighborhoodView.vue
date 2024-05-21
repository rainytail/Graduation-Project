<template>
<ContentBase>
    <h5 style="display:inline-block;">社区动态...</h5>
    <button @click="showModal = true" style="display:inline-block; position: absolute; top: 10px; right: 10px; margin: 5px" type="button" class="btn btn-info">发布...</button>
    <br>
    <div v-for="share in all_share" :key="share.userId" class="container text-center">
        <div class="card">
            <div class="card-body">
                <div class="row">
                    <div class="col-4">
                        <!-- 头像 -->
                        <UserCard :share="share"></UserCard>
                    </div>
                    <div class="col-8">
                        <!-- 发布 -->
                        <ShareContent style="width: 100%; height: 100%;" :share="share"></ShareContent>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 模态对话框 -->
    <div v-if="showModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="showModal = false">&times;</span>
            <p>选择文件并上传</p>
            <div class="input-group mb-3">
                <span class="input-group-text">Title</span>
                <input type="text" ref="title" class="form-control">
            </div>
            
            <div class="input-group mb-3">
                <input @change="handleFileUpload" type="file" class="form-control" id="selectFile">
                <label class="input-group-text" for="selectFile">Post</label>
            </div>

            
            <div class="input-group">
                <span class="input-group-text">Content</span>
                <textarea ref="textarea" class="form-control" placeholder="输入你的想法..." aria-label="With textarea"></textarea>
            </div>

            <!-- 上传文件的按钮 -->
            <button @click="post_submit" style="width: 30%; margin-top: 10px;" type="button" class="btn btn-outline-secondary">发表</button>
        </div>
    </div>
</ContentBase>

</template>

<script>
import ContentBase from '../components/ContentBase.vue'
import UserCard from '../components/UserCard.vue'
import ShareContent from '../components/ShareContent.vue'
import $ from 'jquery'
import { ref } from 'vue'
import { useStore } from 'vuex'

export default {
    name: "NeighborhoodView",
    components: {
        UserCard,
        ShareContent,
        ContentBase,
    },
    setup() {
        let store = useStore();

        let all_share = ref({});

        let showModal = ref(false);

        let textarea = ref(null);
        let fileInput = ref(null);
        let title = ref(null);

        
        let selece_file = ref({ name: '' });

        $.ajax({
            url: 'http://81.70.183.49:8000/vueApi/getneighborhood/',
            type: 'get',
            success(resp) {
                all_share.value = resp.all_share;
                console.log("share ajax: ", all_share.value);
            }
        });

        const post = () => {
            showModal.value = true;
        };

        const triggerFileInput = () => {
            console.log(fileInput.value);
            fileInput.value.click();
            // fileInput;
            // console.log('tg input');
        }

        const handleFileUpload = (event) => {
            selece_file.value = event.target.files[0];
            console.log("选择的文件是: ", selece_file.value.name);
        };

        const re_get = () => {
            $.ajax({
                url: 'http://81.70.183.49:8000/vueApi/getneighborhood/',
                type: 'get',
                success(resp) {
                    all_share.value = resp.all_share;
                    console.log("share ajax: ", all_share.value);
                }
            });
        }

        const post_submit = () => {
            let titleContent = title.value.value;
            let file = selece_file.value;
            let filename = file.name;
            let content = textarea.value.value;

            console.log("title: ", titleContent, ' filename: ', filename, ' content: ', content);

            let user = store.state.user;
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/share_post/",
                type: "POST",
                contentType: 'application/json', // 确保使用 JSON 内容类型
                async: false,
                data: JSON.stringify({
                    userId: user.id,
                    username: user.username,
                    userlabel: user.label,
                    userage: user.age,
                    user_urge: user.urge,
                    avatar: user.avatar,
                    
                    title: titleContent,
                    resourceName: filename,
                    resourceUrl: "/",

                    content: content,
                }),
                success(resp) {
                    if (resp.result === 'success') {
                        alert("发表成功");
                    }
                }
            });
            showModal = false;
            re_get();
        }

        return {
            all_share,
            post,
            textarea,
            showModal,
            triggerFileInput,
            handleFileUpload,
            post_submit,
            title,
        }
    }
}

</script>

<style scoped>
.card {
    user-select: none;
    cursor: pointer; 
    -webkit-transition: all .5s; 
    -moz-transition: all .5s; 
    -ms-transition: all .5s; 
    -o-transition: all .5s; 
    transition: all .5s;
    background-color: white;
    margin-top: 20px;
}
.card:hover {
    background-color: #F6F7F5;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
.modal {
  display: block; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

.modal-content {
  background-color: #fefefe;
  margin: 5% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 60%; /* Could be more or less, depending on screen size */
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
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