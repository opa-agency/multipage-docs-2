import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import './styles/fonts.css'
import './styles/tailwind.css'

const app = createApp(App)

app.use(router)
app.mount('#app')
