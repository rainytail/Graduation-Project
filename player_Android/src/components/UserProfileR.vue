<!-- 设置 -->
<template>
    <div class="container">
        <div class="card">
            <div class="card-body">
                <div class="container">
                    <ul style="list-style: none;">
                        <li>
                            <span>姓名: </span>
                            <input type="text" id="name">
                        </li>
                        <blockquote></blockquote>
                        <li>
                            <span>签名: </span>
                            <textarea name="label" id="label" cols="30" rows="2"></textarea>
                        </li>
                        <blockquote></blockquote>
                        <p>播放设置</p>
                        <li>
                            <span>播放默认速度</span>
                            <input type="text" name="sudu" id="sudu">
                        </li>
                        <blockquote></blockquote>
                        <li>
                            <span>播放默认音质</span>
                            <input type="text" name="yinzhi" id="yinzhi">
                        </li>
                    </ul>
                    <button>修改</button>
                </div>
            </div>
        </div>
    </div>  
</template>

<script>
import ContentBase from './ContentBase.vue';

export default {
    name: "UserProfileR",
    components: ContentBase,
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