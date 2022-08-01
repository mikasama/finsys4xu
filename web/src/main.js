import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'

// import axios from 'axios'

// Vue.prototype.$axios = axios  // 挂载在vue实例上
// Vue.use(axios)   不需要配置，axios也可以用，不知为何？

Vue.config.productionTip = false
Vue.use(ElementUI)

new Vue({
  render: h => h(App),
}).$mount('#app')
