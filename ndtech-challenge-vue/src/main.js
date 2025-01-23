import { createApp } from "vue";
import { createVuetify } from "vuetify";
import { createPinia } from "pinia";
import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import "./style.css";
import App from "./App.vue";
import router from "./utils/router";

const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
          mdi,
        },
      },
  })
const _pinia = createPinia() 
const app = createApp(App);
app.use(vuetify);
app.use(_pinia)
app.use(router);
app.mount("#app");
