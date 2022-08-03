import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
// 引入router
import router from './router/index.js'

// import axios from 'axios'

// Vue.prototype.$axios = axios  // 挂载在vue实例上
// Vue.use(axios)   不需要配置，axios也可以用，不知为何？

Vue.config.productionTip = false
Vue.use(ElementUI)

new Vue({
  //  将router注入到vue示例对象上
  router,
  render: h => h(App),
}).$mount('#app')
