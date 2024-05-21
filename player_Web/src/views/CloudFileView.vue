<template>
    <!-- <ContentBase> -->
        <ContentBase>
                <div class="container text-center">
                    <div class="row">
                        <div class="col-3">
                            <div class="card">
                                <div class="card-body d-flex flex-column mb-3">
                                    <div class="p-2">
                                        <UserInfo></UserInfo>
                                    </div>
                                    <div class="p-2">
                                        <button @click="delete_cloudfiles" type="button" class="btn btn-outline-secondary option">删除文件</button>
                                        <button @click="showModal = true" type="button" class="btn btn-outline-secondary option">上传文件</button>
                                        <button @click="refresh_files" type="button" class="btn btn-outline-secondary option">刷新云盘</button>
                                    </div>
                                    <!-- <div class="p-2">Flex item 3</div> -->
                                </div>
                            </div>
                        </div>
                        <div id="showfiles" :key="componentKey" class="col-9">
                            <ContentBase>
                                <nav aria-label="breadcrumb">
                                    <ol class="breadcrumb">
                                        <li v-for="v in now_dir2" :key=v class="breadcrumb-item active" style="font-size: 20px; text-align: center; user-select: none;" aria-current="page">
                                            {{ v }}
                                        </li>
                                    </ol>
                                </nav>
                            </ContentBase>
                            <br>
                            <div v-if="cloudfiles.length != 0" class="card">
                                <div style="float: left" class="card-body">
                                    <button style="float: left" @click="returnUp" type="button" class="btn btn-outline-secondary choice">上一级</button>
                                    <button style="float: left" v-if="!show_check" @click="show_check = true" type="button" class="btn btn-outline-secondary choice">选择文件</button>
                                    <button style="float: left" v-if="show_check" @click="show_check = false" type="button" class="btn btn-outline-secondary choice">取消</button>
                                    <button style="float: left" v-if="!show_check" @click="create_folder" type="button" class="btn btn-outline-secondary choice">新建文件夹</button>
                                    <br/> <br/>
                                    <div v-for="cloudfile in cloudfiles" :key="cloudfile.filename" class="card">
                                        <div class="card-body">
                                            <div class="container text-center">
                                                <div class="row">
                                                    <div class="col-1">
                                                        <div v-if="show_check && cloudfile.is_dir === 'false'" class="form-check">
                                                            <input class="form-check-input" v-model="selectedItems"  type="checkbox" :value="cloudfile.fileId">
                                                        </div>
                                                    </div>
                                                    <div id="filename" class="col-1">
                                                        <img src="../../public/images/audio.png" style="width:100%" v-if="cloudfile.is_dir === 'false'" alt="">
                                                        <img src="../../public/images/dir.png" style="width:100%" v-if="cloudfile.is_dir === 'true'" alt="">
                                                    </div>
                                                    <div id="filename" class="col-5">
                                                        {{ cloudfile.filename }}
                                                    </div>
                                                    <div class="col-5">
                                                        <button v-if="cloudfile.is_dir === 'false'" @click="viewSource(cloudfile)" type="button" class="btn btn-outline-primary file-op">前往预览</button>
                                                        <button v-if="cloudfile.is_dir === 'false'" @click="download(cloudfile)" type="button" class="btn btn-outline-primary file-op">下载</button>
                                                        <button v-if="cloudfile.is_dir === 'false'" @click="copyToClipboard(cloudfile)" type="button" class="btn btn-outline-primary file-op">复制文件链接</button>
                                                        <button v-if="cloudfile.is_dir === 'true'" @click="indir(cloudfile)" type="button" class="btn btn-outline-primary file-op">进入</button>
                                                        <button v-if="cloudfile.is_dir === 'true'" @click="del_folder(cloudfile)" type="button" class="btn btn-outline-primary file-op">删除文件夹</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-if="cloudfiles.length === 0" class="card">
                                <div class="card-body">
                                    <button style="float: left" @click="returnUp" type="button" class="btn btn-outline-secondary choice">上一级</button>
                                    <button style="float: left" v-if="!show_check" @click="show_check = true" type="button" class="btn btn-outline-secondary choice">选择文件</button>
                                    <button style="float: left" v-if="show_check" @click="show_check = false" type="button" class="btn btn-outline-secondary choice">取消</button>
                                    <button style="float: left" v-if="!show_check" @click="create_folder" type="button" class="btn btn-outline-secondary choice">新建文件夹</button>
                                    <br> <br>
                                    <div class="card">
                                        <div class="card-body">
                                            <h3>这里暂时还没有文件...</h3>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </ContentBase>

    <!-- 模态对话框 -->
    <div v-if="showModal" class="modal">
        <div class="modal-content">
            <span class="close" @click="showModal = false">&times;</span>
            <p>选择文件并上传</p>
            <input type="text" ref="upload_file_name" placeholder="输入上传的文件名...">
            <!-- 隐藏的文件输入元素 -->
            <input type="file" ref="fileInput" style="display: none;" @change="handleFileUpload">
            <!-- 用户点击的按钮，用于触发文件选择 -->
            <div class="container text-center" style="margin: 10px">
                <div class="row">
                    <div class="col-4">
                        <button @click="triggerFileInput" type="button" class="btn btn-outline-secondary">选择文件</button>
                    </div>
                    <div class="col-8">
                        <h4 id="upload_filename">这里显示选择的文件名</h4>
                    </div>
                </div>
            </div>
            <!-- 上传文件的按钮 -->
            <button @click="uploadFile" style="width: 30%; margin-top: 10px;" type="button" class="btn btn-outline-secondary">上传</button>
        </div>
    </div>

    <!-- </ContentBase> -->
</template>

<script>
import ContentBase from '../components/ContentBase.vue';
import UserInfo from '../components/UserInfo.vue';
import $ from 'jquery';
import { useStore } from 'vuex';
import { ref } from 'vue';
// import Clipboard from 'clipboard';

export default {
    name: "CloudFileView",
    components: {
        ContentBase,
        UserInfo,
    },
    data() {
        return {
            componentKey: 0,
            pre_path: "http://81.70.183.49:8000/static/videos/",
        };
    },
    methods: {
        refresh() {
            // let show_files = document.getElementById('showfiles');
            this.componentKey += 1;
        },
        async copyToClipboard(cloudfile) {
            try {
                await navigator.clipboard.writeText(this.pre_path + cloudfile.filesource);
                alert('复制链接成功');
            } catch (err) {
                console.error('Failed to copy: ', err);
                alert('复制失败');
            }
        }
    },
    setup() {
        const store = useStore();
        let cloudfiles = ref([]);

        let fileInput = ref(null);
        
        let selece_file = ref({ name: '' });

        let showModal = ref(false);
        let show_check = ref(false);

        let upload_file_name = ref(null);

        let selectedItems = ref([]);

        let now_dir = ref('/');
        let now_dir2 = ref(['folder: ']);

        $.ajax({
            url: "http://81.70.183.49:8000/vueApi/get_cloudfiles",
            type: 'get',
            async: false,
            data: {
                userId: store.state.user.id,
                dir: now_dir.value,
            },
            success(resp) {
                cloudfiles.value = resp.cloudfiles;
                cloudfiles.value.sort((a, b) => {
                    return (a.is_dir === b.is_dir) ? 0 : a.is_dir ? -1 : 1;
                });
                console.log(cloudfiles);
                for (let i = 0; i < cloudfiles.value.length; i ++ )
                    console.log(cloudfiles.value[i]);
            },
            error() {
                console.log("api get_cloudfile error");
            }
        });

        const viewSource = (cloudfile) => {
            window.open('http://81.70.183.49:8000/static/videos/' + store.state.user.id + cloudfile.dir + cloudfile.filesource);
        };

        const triggerFileInput = () => {
            console.log(fileInput.value);
            fileInput.value.click();
        };

        const uploadFile = () => {
            if (!selece_file.value || !upload_file_name.value.value) {
                alert("请正确输入，检查是否少输入!");
                return ;
            }
            let option = 0;
            if (confirm('确认上传文件?')) {
                option = 1;
            } else {
                option = 0;
            }
            if (!option) {
                showModal.value = false;
                return ;
            }
            const file = selece_file.value;
            const formData = new FormData();
            formData.append('file', file);
            formData.append('userId', store.state.user.id);
            formData.append('filename', upload_file_name.value.value);
            formData.append('filesource', file.name);
            formData.append('dir', now_dir.value);
            formData.append('is_dir', 'false');

            $.ajax({
                url: 'http://81.70.183.49:8000/vueApi/upload/',
                type: 'post',
                data: formData,
                async: false,
                processData: false,  // 告诉jQuery不要处理发送的数据
                contentType: false,  // 告诉jQuery不要设置Content-Type请求头
                success: function(response) {
                    console.log('File uploaded successfully', response);
                    console.log(response);
                },
                error: function(xhr, status, error) {
                    console.error('Error uploading file', error);
                }
            });

            showModal.value = false;
            re_get();
            alert("上传成功！");
        };

        const handleFileUpload = (event) => {
            selece_file.value = event.target.files[0];
            let div_filename = document.querySelector('#upload_filename');
            if (!div_filename) console.log("没有找到filename h");
            else console.log("div_filename: ", div_filename);
            div_filename.textContent = selece_file.value.name;
            console.log("选择的文件是: ", selece_file.value.name);
        };

        // const pushFile = (file) => {
            
        // },

        const delete_cloudfiles = () => {
            if (selectedItems.value.length === 0) {
                alert("未选择文件!");
                return ;
            }
            let option = 0;
            if (confirm('确认删除?')) {
                option = 1;
            } else {
                option = 0;
            }
            if (!option) {
                return ;
            }
            console.log("delete: ", selectedItems.value);
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/delete_files/",
                type: 'POST',
                contentType: 'application/json',  // 确保设置为 application/json
                data: JSON.stringify({  // 确保数据被序列化为 JSON 字符串
                    'fileIds': selectedItems.value,
                }),
                success(resp) {
                    console.log(resp.result);
                    alert("删除成功!");
                    re_get();
                },
                error(xhr, status, error) {
                    console.error('Error: ', error);
                }
            })
        };

                // 使用XmlHttpRequest来请求后端api，使用jquery的ajax则会导致blob数据无法被辨认
        const download = (audio) => {
            const url = 'http://81.70.183.49:8000/static/videos/' + String(store.state.user.id + audio.dir + audio.filesource); // 替换为你的后端 URL
    
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url);
            // blob数据即为大二进制数据，用于存储音频、视频、图像等
            xhr.responseType = 'blob'; // 告诉 XMLHttpRequest 返回的数据类型是 Blob 对象
            
            xhr.onload = function() {
                if (xhr.status === 200) {
                    // 创建一个 <a> 元素
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(xhr.response);
                    link.download = audio.filename; // 设置下载文件的名称
                    
                    // 模拟点击这个 <a> 元素来触发下载
                    link.click();
                } else {
                    console.error('Request failed with status:', xhr.status);
                }
            };
            
            xhr.send();
        };

        const re_get = () => {
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/get_cloudfiles",
                type: 'get',
                async: false,
                data: {
                    userId: store.state.user.id,
                    dir: now_dir.value,
                },
                success(resp) {
                    cloudfiles.value = resp.cloudfiles;
                    cloudfiles.value.sort((a, b) => {
                        return (a.is_dir === b.is_dir) ? 0 : a.is_dir ? -1 : 1;
                    });
                    console.log(cloudfiles);
                    for (let i = 0; i < cloudfiles.value.length; i ++ )
                        console.log(cloudfiles.value[i]);
                },
                error() {
                    console.log("api get_cloudfile error");
                }
            });
        };

        const refresh_files =  () => {
            re_get();
        };

        const create_folder = () => {
            const userInput = prompt('输入文件夹名称: ');
            if (userInput !== null) {
                // 用户点击"确定"，userInput 包含输入的文本
                // alert(`您输入的是: ${userInput}`);
                $.ajax({
                    url: "http://81.70.183.49:8000/vueApi/create_folder/",
                    type: 'get',
                    data: {
                        userId: store.state.user.id,
                        folder_name: userInput,
                        dir: now_dir.value,
                    },
                    success() {
                        console.log("create success");
                    }
                });
                alert("创建成功")
                re_get();
            } else {
                // 用户点击"取消"
                alert('取消输入');
            }
        };

        const del_folder = (folder) => {
            let option = 0;
            if (confirm('确认删除?')) {
                option = 1;
            } else {
                option = 0;
            }
            if (!option) {
                return ;
            }
            console.log("dir: ", now_dir.value, ' folder_name: ', folder.filename, ' userId: ', store.state.user.id);
            $.ajax({
                url: "http://81.70.183.49:8000/vueApi/delete_folder/",
                type: 'get',
                data: {
                    dir: now_dir.value,
                    folder_name: folder.filename,
                    userId: store.state.user.id,
                },
                success(resp) {
                    if (resp.result === "success") {
                        console.log(resp);
                        alert("删除成功!");
                        re_get();
                    }
                }
            })
        };

        const indir = (folder) => {
            now_dir.value += folder.filename + '/';
            now_dir2.value.push(folder.filename);
            console.log("folder name: ", folder.folder_name);
            re_get();
        };

        const returnUp = () => {
            if (now_dir2.value.length === 1) return ;
            let len = now_dir2.value[now_dir2.value.length-1].length;
            // now_dir.value = "/123/";
            now_dir.value = now_dir.value.substring(0, now_dir.value.length - len - 1);
            // 修改now_dir now_dir2
            now_dir2.value.pop();
            console.log("now_dir: ", now_dir);
            re_get();
        }

        return {
            cloudfiles,
            viewSource,
            triggerFileInput,
            handleFileUpload,
            fileInput,
            uploadFile,
            showModal,
            upload_file_name,
            show_check,
            delete_cloudfiles,
            selectedItems,
            download,
            refresh_files,
            create_folder,
            indir,
            del_folder,
            now_dir2,
            returnUp,
        }
    }
}

</script>

<style scoped>
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
  margin: 15% auto; /* 15% from the top and centered */
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

.option {
    margin: 10px;
    width: 80%;
}

.choice {
    margin-right: 10px;
}

.file-op {
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
</style>