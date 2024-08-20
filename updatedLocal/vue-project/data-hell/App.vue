<script setup>
import node from './components/node.vue'
import axios from 'axios'
import data from './out.json';
import { ref, onMounted } from 'vue'
const currentActive = ref(0)
const outed = ref(["name", "major", "origin"]) 
onMounted(() => {
  addEventListener("keypress", (event) => {
    var code = document.getElementById("code").innerText;
    switch(event.key){
      case "1":{
        document.getElementById('name-'+code).value = window.getSelection().toString();
        break;
      }
      case "2":{
        document.getElementById('major-'+code).value = window.getSelection().toString();
        break;
      }
      case "3":{
        document.getElementById('origin-'+code).value = window.getSelection().toString();
        break;
      }
    }
  });
})
// window.getSelection().toString()

</script>
<template>
  <body>
      <span hidden id="code">{{data[currentActive].code}}</span>
      <div class="list" :style="'transform:translateX('+82*-(currentActive-(data.length-1)/2)+'vh);'">
        <node :post="data[data.length-1]" :i="-1"/>
        <node v-for="(item, i) in data" :post="item" :i="i" :active="(i == currentActive)"/>
        <node :post="data[0]" :i="-1"/>
      </div>
      <button style="left:0%; right:90vw" @click="currentActive--; if(currentActive<0)currentActive=data.length-1"><</button>
      <button style="left:90vw; right:0%" @click="currentActive++; if(currentActive>data.length-1)currentActive=0">></button>
</body>
</template>

<style scoped>
.list{
  display: flex;
  position: sticky;
  justify-content: space-around;
  height: 100%;
  align-items: center;
  position: static;
  transition: all .3s ease-in-out;
}
button{
  position: fixed;
  background-color: rgba(0, 0, 0, 0);
  border: none;
  font-size: 10vh;
  top: 0;
  bottom: 0;
}
body{
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: darkslategrey;
  margin: 0;
}
</style>
