import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import { useAuthStore } from './store'

const routes = [
  { path: '/', component: HomeView, meta: { requiresAuth: true }  },
  { path: "/login", component: LoginView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})


router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login"); 
  } else {
    next();
  }
});
export default router