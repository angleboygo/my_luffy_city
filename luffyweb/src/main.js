// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

// 导入gt极验
import '../static/globals/gt.js'

//导入地区
import '../static/globals/nation.js'


// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import router from './routers/index'
Vue.config.productionTip = false


//调用插件
Vue.use(ElementUI)
Vue.config.productionTip=false

//配置axios
import axios from 'axios'; // 从node_modules目录中导入包
Vue.prototype.$axios = axios; // 把对象挂载vue中


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
