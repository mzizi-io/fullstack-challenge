import { defineStore } from "pinia";
import { ref } from "vue";

export const useGlobalStore = defineStore("global", () => {
  const assets = ref([]);
  const pageCount = ref(100)
  const page = ref(1)
  const perPage = ref(10)
  const maxEstimatedValue = ref(1000)

  const setAssets = (newVal) =>{
    assets.value = newVal
  }

  const setPage = (newVal) =>{
    page.value = newVal
  }

  const setPerPage = (newVal) =>{
    perPage.value = newVal
  }

  const setPageCount = (newVal) =>{
    pageCount.value = newVal
  }

  const setMaxEstimatedValue = (newVal) =>{
    maxEstimatedValue.value = newVal
  }

  return { 
    assets,
    setAssets, 
    pageCount,
    setPageCount, 
    maxEstimatedValue, 
    setMaxEstimatedValue,
    page, 
    setPage,
    perPage,
    setPerPage
  };
});


export const useAuthStore = defineStore("auth", () => {
  const isAuthenticated = ref(!!localStorage.getItem("token"));

  const login = (token) => {
    isAuthenticated.value = true;
    localStorage.setItem("token", token);
  };

  const logout = () => {
    isAuthenticated.value = false;
    localStorage.removeItem("token");
  };

  return { isAuthenticated, login, logout };
});