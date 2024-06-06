import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/tailwind.css'
import './assets/style.css'
import axios from 'axios'
import globalMixin from './globalMixin.js';


axios.defaults.baseURL = 'http://127.0.0.1:8000'
store.commit('initializeStore');
const app = createApp(App);

// Register the global mixin
app.mixin(globalMixin);

// Mount the app with router and store
app.use(store).use(router,axios).mount('#app');
