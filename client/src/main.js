import { createApp } from 'vue'
import App from './App.vue'
import Vue3Autocounter from 'vue3-autocounter'

require("./assets/main.scss")

createApp(App)
    .component('vue3-autocounter', Vue3Autocounter)
    .mount('#app')
