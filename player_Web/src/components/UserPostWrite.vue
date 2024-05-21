<template>
    <div class="card edit-field">
        <div class="card-body">
            <!-- <label for="edit-post" class="form-label">发帖</label> -->
            <!-- 使用v-model来绑定content值 -->
            <textarea v-model="content" class="form-control" id="edit-post" rows="3"></textarea>
            <button @click="post_a_post" type="button" class="btn" style="margin-top: 10px;">发送</button>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue'

export default {
    name: "UserPostWrite",

    setup(props, context) {
        let content = ref('');

        const post_a_post = () => {
            if (content.value === '') return ;
            context.emit('post_a_post', content.value);
            content.value = '';
        };
        
        return {
            content,
            post_a_post,
        }
    }
}
</script>

<style scoped>
.edit-field {
    margin-top: 10px;
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