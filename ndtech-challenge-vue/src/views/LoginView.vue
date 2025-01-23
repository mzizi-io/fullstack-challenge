<template>
    <div class="login-container">
      <h2>Login</h2>
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <v-btn @click="handleLogin" color="light-blue-lighten-3">Login</v-btn>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
    import { useAuthStore } from "../utils/store";
  
  const router = useRouter();
  const authStore = useAuthStore();
  const username = ref("");
  const password = ref("");
  const errorMessage = ref("");
  
  const handleLogin = () => {
    if (username.value === "admin" && password.value === "password") {
      authStore.login("authToken");
      router.push("/");
    } else {
      errorMessage.value = "Invalid username or password";
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-width: 300px;
    margin: auto;
  }
  </style>
  