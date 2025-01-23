<script setup>
import { ref } from 'vue'
import logo from "../../src/assets/img/logo.webp"
</script>

<template>
  <div class="navbar-container">
    <div>
      <RouterLink to="/">
        <img class="logo" :src=logo alt="logo"/>
      </RouterLink>
    </div>
  </div>

</template>

<style scoped>
.navbar-container {
    height: 70px;
    padding-left: 2rem;
    display: flex;
    align-items: center;
    justify-content:space-between;
    position: absolute;
    top: 0;
    width: 100%;
    background-color: #0C2F57;
}
.link {
  text-decoration: none;
  color: white;
  font-size: 1.3rem;
}
.link:hover{
  font-weight: bold;
  color: #41B6E6;
}

.logo {
  height: 50px;
  width: 50px
}
.right {
  display: flex;
  gap: 2rem;
  float: right;
  width: 20rem;
}
</style>
