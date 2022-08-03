import Vue from 'vue'
import {Router, VueRouter} from 'vue-router'
import wencai from '@/components/Wencai.vue'
import city from '@/components/City.vue'

// Vue.use(Router)  // vue全局使用router
Vue.use(VueRouter)  // 第三方库需要use下才能使用

// export default new Router({
//     routes: [
//         {
//             path: "/",
//             name: "wencai",
//             component: wencai
//         },
//         // {
//         //     path: "h1",
//         //     component: Hi,
//         //     children: [
//         //         {path: "/", component: hh1},
//         //         {path: "hhh1", component: hhh1},
//         //         {path: "hhh2", component: hhh2},
//         //     ]
//         // },
//     ]
// })


// 定义routes路由集合，数组类型
const routes = [
    {path: '/wencai', component: wencai},
    {path: '/city', component: city}
]

// 实例化VueRouter并将routes添加进去
const router=new VueRouter({
    // ES6简写，等于routes：routes
    routes
})

// 抛出这个示例对象，方便外部读取和访问
export default router