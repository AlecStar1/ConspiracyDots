<script setup>
import { ref, watch, h, onMounted} from 'vue'
import VueSocial from "@growthbunker/vuesocial";
const props = defineProps({
  code: {
    type: String,
    required: true
  },
  data: {
    type: Object,
    required:false
  }
})  
// name : String
// gender : 1:male 2:female 3:other
// major : string
// from : string
// hobbies : array
// committed : 1,2,3
// Music : array
// contact : object
// roommate : bool
</script>
<template>
  <div class="container">
    <div class="name">
      <h1>{{ data['name'] }}</h1>
      <h4>from: {{ data['from']}}</h4>
    </div>
    <div class="Hobbies">
      <ul>
        <li v-for="f in data['hobbies']">{{f}}</li>
      </ul>
    </div>
    
  </div>
</template>

<style scoped>

  .container {  display: grid;
    position: fixed !important;
    grid-template-columns: 0.7fr 1.3fr 1fr;
    grid-template-rows: 0.5fr 1fr 1fr;
    grid-auto-columns: 1fr;
    gap: 0px 0px;
    grid-auto-flow: row;
    grid-template-areas:
      "name name name"
      "Hobbies . ."
      ". . .";
  }
  
  .name { 
    grid-area: name; display: flex; 
    flex-direction: column;
    justify-content: center; 
    align-content: center;
    align-items: center;
  }
  h1, h4 {
    padding: 0%;
    margin: 0;
    background-color: rgba(181, 238, 255, 0.315);
    width: 100%;
    text-align: center;
  }
  ul{
    background-color: rgba(181, 238, 255, 0.315);
    height: 100%;
  }

  .Hobbies { grid-area: Hobbies; }
  
</style>
