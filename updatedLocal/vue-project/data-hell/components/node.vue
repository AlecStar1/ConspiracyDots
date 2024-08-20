<script setup>
import infoPanel from './infoPanel.vue'
import axios from 'axios';
import { ref, onMounted } from 'vue'
const props = defineProps({
  post: {
    type: Object,
    required: true
  },
  active:{
    type:Boolean,
    default:false
  },
  i:{
    type:Number,
    required:false
  }
})
var info = "";
onMounted(async ()=>{
  await axios
    .get('./data/'+props.post.code+'.json')
    .then(response => (info = response['data']))
})
</script>
<template>
  <div :style="'opacity:'+(active?1:0.3)+';'">
    <infoPanel :code="(i != -1)?post.code:''+Math.random()" :data="info"/>
    <img width="110%" height="110%" :src='"ims/"+post.code+".jpg"' />
    <a>
      {{ post.caption_text }}
    </a>
  </div>
</template>

<style scoped>
  div {
    width: 80vh;
    height: 80vh;
    
    margin: 1vh;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50px;
    flex: none;
    overflow: hidden;
    position: relative;
    outline: solid black 5px;
  }
  a {
    position:absolute;
    background-color: rgba(128, 128, 128, 0.642);
    
    color: whitesmoke;
    font-family: "Work Sans", sans-serif;
    transform: translateY(100px);
  }
  img {
    border-radius: 50px;
  }
</style>
