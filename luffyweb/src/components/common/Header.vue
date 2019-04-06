<template>
  <div class="header">
    <el-container>
      <el-header height="80px">
        <el-row>
          <!-- 左 -->
          <el-col :span="3" class="logo">
            <router-link to="/">
              <img src="../../assets/head-logo.a7cedf3.svg" alt>
            </router-link>
          </el-col>
          <!-- 中 -->
          <el-col :span="16">
            <el-row class="nav" :gutter="20">
              <el-col :span="3"><router-link to="/courses">免费课</router-link> </el-col>
              <el-col :span="3">轻课</el-col>
              <el-col :span="3">学位课</el-col>
              <el-col :span="3">题库</el-col>
              <el-col :span="3">老男孩教育</el-col>
            </el-row>
          </el-col>
          <!-- 右 -->
          <el-col class="login-bar" :span="5">
            <el-row :gutter="20">
              <el-col class="cart-ico" :span="6">
                <b>2</b>
                <img src="../../assets/shopping.svg" alt>
                <span><router-link to="/cart">购物车</router-link></span>
              </el-col>
              <el-col v-if="is_login==false" class="study" :span="10"><span><router-link to="/login">登录</router-link></span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<span class='header-register'><router-link to='/register'>注册</router-link></span></el-col>
             
              <div v-else>
                <el-col class="study" :span="10">学习中心</el-col>
             
              <el-col   :span="8">
                <el-dropdown class='user-box'>
                  <span class="el-dropdown-link">
                    <img src="../../assets/logo@2x.png" alt>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>我的账户</el-dropdown-item>
                    <el-dropdown-item>我的订单</el-dropdown-item>
                    <el-dropdown-item>我的优惠券</el-dropdown-item>
                    <el-dropdown-item>我的消息<b style='color'>0</b></el-dropdown-item>
                     <el-dropdown-item><span @click="logout">退出登录</span> <i class="el-icon-arrow-right"></i></el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </el-col>
              </div>
            </el-row>
          </el-col>
        </el-row>
      </el-header>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Headers",
  data() {
    return {
      token:localStorage.token||sessionStorage.token,
      is_login:false,
    };
  },
  created(){
    if(this.token){
      this.is_login=true;

    }else{
      this.is_login=false;
    }
  },
   methods:{
      logout(){
        localStorage.clear();
        sessionStorage.clear();
        this.is_login=false;
        alert("退出登录成功");
      }
    }
};
</script>


<style  scoped>
.header {
  width: 100%;
  height: 80px;
  background: #fff;
  position: fixed;
  left: 0;
  top: 0;
  margin: 0 auto;
  z-index: 7;
  text-overflow: ellipsis;
  font-size: 16px;
  white-space: nowrap;
  box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
}

.el-container {
  width: 1200px;
  margin: 0 auto;
  line-height: 80px;
}

.el-container img {
  vertical-align: middle;
      width: 118px;
    height: auto;
    cursor: pointer;

}

.el-header {
  padding: 0;
}

.header .nav,
.header .login-bar {
  text-align: center;
}

.header .nav span {
  color: #4a4a4a;
}

.nav .el-col:hover,.nav .el-col a:hover {
  color: green;
}
.login-bar{
    font-size: 14px;
}

.login-bar .study{
    font-size: 14px;
    cursor: pointer;
    display: inline-block;
}

.login-bar img {
  width: 26px;
  height: 26px;
  border-radius: 50%;
}
.login-bar img:hover {
  border: 1px solid rgb(255, 194, 16);
}

/* .login-bar .user-box{
    padding: 0;
    position: absolute;
     left: 180px; 
} */
.el-col-8 {
    width: 14%;
}
.cart-ico {
  width: 88px;
  height: 28px;
  margin-top: 26px;
  background: #f7f7f7;
  border-radius: 17px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  cursor: pointer;
  position: relative;
  font-size: 14px;
}

.cart-ico:hover{
    background: #f0f0f0
}
.cart-ico img {
  width: 15px;
  height: auto;
  margin-left: 6px;
}
.cart-ico b {
  width: 16px;
  height: 16px;
  line-height: 17px;
  font-size: 12px;
  color: #fff;
  text-align: center;
  background: #fa6240;
  border-radius: 50%;
  transform: scale(0.8);
  position: absolute;
  left: 16px;
  top: -1px;
}

.el-dropdown-menu{
    width: 180px;
    position: absolute;
    left: 1378px!important;
    top: 80px;
    z-index: 100;
    background: #fff;
    border-top: 2px solid #d0d0d0;
    box-shadow: 0 2px 4px 0 #e8e8e8;
}


.el-dropdown-menu b{
    font-size: 12px;
    display: inline-block;
    color: #ee6723;
    line-height: 18px;
    font-weight: 400;
    transform: scale(.9);
    margin-left: 2px;
    font-family: PingFangSC-Regular;
}

</style>

