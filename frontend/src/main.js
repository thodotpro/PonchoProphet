import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router.js'

import './assets/styles/tokens.css'
import 'bulma/css/bulma.min.css'
import './assets/styles/bulma-overrides.css'
import './assets/styles/global.css'

createApp(App).use(router).mount('#app')
