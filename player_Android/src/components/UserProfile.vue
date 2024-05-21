<template>
    <div class="card">
        <div class="card-body" style="width: 50%;">
            这里写内容
        </div>
    </div>
</template>

<script>
export default {
    name: "TextContent",
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