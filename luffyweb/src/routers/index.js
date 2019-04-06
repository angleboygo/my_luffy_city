import Vue  from 'vue'
import Router  from 'vue-router'
import { homedir } from 'os';


//这里导入可以让用户访问的组件
import Home from '@/components/Home';
import Courses from '@/components/Courses';
// import Cart from '@/components/Cart';
import Login from '@/components/Login';
import Register from '@/components/Register';

Vue.use(Router)

export default new Router({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'Home',
            component:Home,
        },
        {
            path:'/home',
            name:'Home',
            component:Home,
        },
        {
            path:'/courses',
            name:'Courses',
            component:Courses,
        },
        // {
        //     path:'/cart',
        //     name:'Cart',
        //     component:Cart,
        // },
        {
            path:'/login',
            name:'Login',
            component:Login,
        },
        {
            path:'/register',
            name:'Register',
            component:Register,
        },
    ]
})
