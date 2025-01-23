<script setup>
import Navbar from "./components/Navbar.vue"
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="app-container">
    <Navbar/>

    <RouterView />
  </div>

</template>

<style scoped>
.app-container {
  height: 100vh;
  overflow:scroll;
  display: flex;
  flex-flow: column; 
}
</style>

