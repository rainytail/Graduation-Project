<template>
    <div class="card" style="width: 18rem;">
    <div class="card-body">
        <h5 class="card-title">镇海中学高三第三次月考英语听力考试</h5>
        <h6 class="card-subtitle mb-2 text-muted">考试分数：28/40</h6>
        <span class="card-text">
            练习次数：3次
        </span>
        &MediumSpace; &MediumSpace;
        <span class="card-text">
            练习情况：已掌握
        </span>
        <a href="#" class="card-link">前往练习</a>
        <a href="#" class="card-link">文章翻译</a>
    </div>
    </div>
</template>

<script>
export default {
    name: "VideoCard",
    
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