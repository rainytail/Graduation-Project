<template>
    <ContentBase>
        <p style="margin: 2px; padding: 2px; text-align: left; font-size: 1.25em;">{{ title }}</p>
        <p style="text-align: left;">{{ resourceName }}</p>
        <!-- <br> -->
        {{ content }}
    </ContentBase>
</template>

<script>
import { reactive } from 'vue';
import ContentBase from './ContentBase.vue';

export default {
    name: "ShareContent",
    props: {
        share: {
            type: Object,
            required: true,
        }
    },
    components: {
        ContentBase,
    },
    setup(props) {
        let share = reactive(props.share);
        let title = share.title;
        let content = share.content;
        let resourceName = share.resourceName;

        return {
            title,
            content,
            resourceName,
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