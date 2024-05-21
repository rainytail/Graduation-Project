<template>
    <div class="card" style="margin-right: 20px;">
        <div class="card-body" style="width: 100%;">
            <textarea @change="change" class="textarea" placeholder="write your note" name="" id="text" cols="60" rows="10"></textarea>
            <button @click.prevent="submit" type="button" class="btn btn-outline-secondary">记录</button>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
import { useStore } from 'vuex';
import { ref } from 'vue';

export default {
    name: "PlayerText",
    setup() {
        let store = useStore();
        let user = store.state.user;
        let content = ref('');

        const change = () => {
            let textarea = document.getElementById('text');
            if (textarea)
                content.value = textarea.value;
            else console.log('textarea not exist');
        };
        

        const submit = () => {
            if (content.value === '') {
                console.log("content为空，提交失败");
                return ;
            }
            $.ajax({
                // 提交一份记录
                url: "http://81.70.183.49:8000/vueApi/insert_a_post/",
                type: "get",
                data: {
                    'userId': user.id,
                    'username': user.username,
                    'title': user.now_listen.name,
                    'content': content.value,
                    'resourceType': user.listen_type,
                    'resourceUrl': user.now_listen.resourceUrl,
                },
                success() {
                    console.log("insert_a_post success");
                }
            });
            return ;
        };

        return {
            submit,
            change,
        }

    }
}
</script>

<style scoped>
blockquote {
    text-align: left;
    font-size: 1.25rem;
}

.textarea {
    background-color: 	#DCDCDC;
    font-size: 18px;

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