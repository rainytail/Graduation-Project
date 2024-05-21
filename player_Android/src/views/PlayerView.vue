<template>
    <div class="container">
        <div class="container card">
            <div class="row">
                <div class="col">
                    <PlayerContent></PlayerContent>
                </div>
                <div class="col">
                    <DictionaryComponent></DictionaryComponent>
                    <PlayerText></PlayerText>
                </div>
            </div>
            <!-- <TextContent style="float: left; width: 50%;"></TextContent> -->
        </div>
    </div>
</template>

<script>
import PlayerContent from '../components/Player.vue';
// import TextContent from '../components/TextContent.vue'
import PlayerText from '../components/PlayerContent.vue'
import DictionaryComponent from '../components/Dictionary.vue'

export default {
    name: 'PlayerView',
    components: {
        PlayerContent,
        // TextContent,
        PlayerText,
        DictionaryComponent,
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