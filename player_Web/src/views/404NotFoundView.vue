<template>
    <ContentBase>
        404页面没有找到
    </ContentBase>
</template>

<script>
import ContentBase from '../components/ContentBase.vue';

export default {
    name: 'NotFoundView',
    components: {
        ContentBase,
    }
}
</script>

<style scoped>
.container {
    margin-top: 20px;
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