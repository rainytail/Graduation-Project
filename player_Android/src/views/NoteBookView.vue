<!-- 用来列出自己收藏/保存的所有音频文件 -->

// TODO Model and Notebook

<template>
    <ContentBase>
        <div v-for="note in notebook" class="card" v-bind:key="note.userId" style="margin-top: 10px;">
            <div class="card-body">
                <div class="row">
                    <div class="col">
                        <p>{{ note.title }}</p>
                    </div>
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                {{ note.content }}
                            </div>
                        </div>
                        <button @click="golisten(note)" type="button" class="btn btn-primary">再次练习</button>
                    </div>
                </div>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '../components/ContentBase.vue';
import { useStore } from 'vuex';
import $ from 'jquery';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: "NoteBookView",
    components: {
        ContentBase,
    },

    setup() {
        let store = useStore();
        let username = store.state.user.username;
        let router = useRouter();

        let notebook = ref([]);

        // 接口，获取用户的所有保存收藏的音频
        $.ajax({
            url: "http://81.70.183.49:8000/vueApi/getNoteBook",
            type: "get",
            data: {
                username: username,
            },
            success(resp) {
                notebook.value = resp.notebook;
            }
        });

        const golisten = (note) => {
            store.commit("changeListen", {
                "resourceName": note.title,
                ...note,
            });
            router.replace({ name: "player" });
        };

        return {
            notebook,
            golisten,
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
}
.card:hover {
    background-color: #F6F7F5;
}
</style>