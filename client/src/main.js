import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory} from 'vue-router'
import ToastPlugin from 'vue-toast-notification';
import App from './App.vue'

import 'vue-toast-notification/dist/theme-bootstrap.css';

import Scanner from '@/components/Scanner.vue'
import Books from '@/components/Books.vue'
import About from '@/components/About.vue'
import Contact from '@/components/Contact.vue'

const routes = [
    { path: '/', component: Scanner },
    { path: '/books', component: Books },
    { path: '/about', component: About },
    { path: '/contact', component: Contact },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

const pinia = createPinia()
const app = createApp(App)

app.config.globalProperties.$NTFY_ENABLED = 1;

app.use(pinia)
app.use(ToastPlugin)
app.use(router)
app.mount('#app')
