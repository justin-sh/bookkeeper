import './assets/main.css'

import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from './App.vue'
import router from './router'

import { library} from "@fortawesome/fontawesome-svg-core"
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome"
import {faCoins, faAngleUp} from "@fortawesome/free-solid-svg-icons"

library.add(faCoins, faAngleUp)

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)
app.component('vue-date-picker', VueDatePicker)

app.use(createPinia())
app.use(router)

app.mount('#app')
