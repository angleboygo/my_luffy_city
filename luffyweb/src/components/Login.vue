<template>
  <div class="login box">
		<img src="https://www.luffycity.com/static/img/Loginbg.3377d0c.jpg" alt="">
		<div class="login">
			<div class="login-title">
				<img src="https://www.luffycity.com/static/img/Logotitle.1ba5466.png" alt="">
				<p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
			</div>
			<div class="login_box">
				<div class="title">
					<span @click="login_type=1" :class="login_type==1?'current':''">密码登录</span>
					<span @click="login_type=2" :class="login_type==2?'current':''">短信登录</span>
				</div>
				<div class="inp" :class="login_type==1?'show':''">
					<input v-model = 'username' type="text"  placeholder="用户名 / 手机号码" class="user">
					<input v-model = 'password' type="password" name="" class="pwd" placeholder="密码">
					<div id="geetest" title="验证码"></div>
					<div class="rember">
						<p>
							<input type="checkbox" class="no" name="a" v-model="remember"></input>
							<span>记住密码</span>
						</p>
						<p>忘记密码</p>
					</div>
					<button class="login_btn" @click="loginhander">登录</button>
					<p class="go_login" >没有账号 <span><router-link to='/register'>立即注册</router-link></span></p>
				</div>

        <div class="inp" :class="login_type==2?'show':''">
					<input v-model = 'mobile' type="text"  placeholder="手机号码" class="user">
					<input v-model = 'sms' type="password" name="" class="pwd" placeholder="短信验证码">
          <div class="rember">
						<p>
							<input type="checkbox" class="no" name="a"></input>
							<span>记住密码</span>
						</p>
						<p>忘记密码</p>
					</div>
					<button class="login_btn">登录</button>
					<p class="go_login" >没有账号 <span><router-link to='/register'>立即注册</router-link></span></p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
  export default{
    name:"Login",
    data(){
      return {
            remember: false,  // 是否记住密码
          login_type:1,     // 登陆方式
          username:"",      // 登陆账号
          password:"",      // 登陆密码
          mobile:"",        // 手机号码
          sms:"",           // 手机短信验证码
          validateResult:false, // 验证码验证状态，默认没有通过验证
      }
    },
    components:{

    },
    methods:{
      // 登陆提交
      loginhander(){    
        // 提交数据前判断用户是否通过了验证码校验 
        if (this.validateResult){
          this.$axios.post('http://api.luffycity.cn:8000/users/login/',{
          'username':this.username,
          'password':this.password,
                 
        },{
          responseType:'json',
        }).then(response=>{
          console.log(response);
          // console.log(this.remember);
          // 请求成功，保存登陆状态
          if(this.remember){
            //记住密码
            sessionStorage.removeItem('token');
            let data = response.data;
            localStorage.token=data.token;
            localStorage.id=data.id;
            localStorage.username = data.username;  
          }else{
            // 不记住密码
            localStorage.removeItem('token');
            let data=response.data;
            sessionStorage.token=data.token;
            localStorage.id=data.id;
            localStorage.username = data.username;  
          }
          //登录成功页面跳转
          this.$router.go(-1);
        }).catch(error=>{
          console.log(error);
        }); 
        }else{
          alert('验证码不正确!')
        } ;
        
      },


      handlerPopup(captchaObj){
        // 成功的回调
         let _this = this;
        captchaObj.onSuccess(function () {
          _this.validateResult=true;
    
        });
        captchaObj.appendTo("#geetest");
      } ,   
    },
  
    created(){
      // 显示图片验证码
      this.$axios.get("http://127.0.0.1:8000/users/verify/").then(response=>{
            // 请求成功
            let data = response.data;
            // 使用initGeetest接口
            // 参数1：配置参数
            // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
            console.log(response.data);
            data = JSON.parse(data);
            initGeetest({
                gt: data.gt,
                challenge: data.challenge,
                product: "embed", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
                offline: !data.success // 表示用户后台检测极验服务器是否宕机，一般不需要关注
                // 更多配置参数请参见：http://www.geetest.com/install/sections/idx-client-sdk.html#config
            }, this.handlerPopup);
      }).catch(error=>{
        console.log(error)
      })
    },
  }
</script>

<style scoped>
.box{
	width: 100%;
	position: relative;

}
.box img{
	width: 100%;
}
.box .login {
	position: absolute;
	width: 500px;
	height: 400px;
	top: 50%;
	left: 50%;
	margin-left: -250px;
	margin-top: -300px;
}
.login .login-title{
     width: 100%;
    text-align: center;
}
.login-title img{
    width: 190px;
    height: auto;
}
.login-title p{
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
}
.login_box{
    width: 400px;
    height: auto;
    background: #fff;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
}
.login_box .title{
	font-size: 20px;
	color: #9b9b9b;
	letter-spacing: .32px;
	border-bottom: 1px solid #e6e6e6;
	 display: flex;
    	justify-content: space-around;
    	padding: 50px 60px 0 60px;
    	margin-bottom: 20px;
    	cursor: pointer;
}
.login_box .title .current{
	    color: #4a4a4a;
    	border-bottom: 2px solid #84cc39;
}

.inp{
	width: 350px;
	margin: 0 auto;
  display: none;
}
.show{
  display: block;
}
.inp input{
    border: 0;
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}
.inp input.user{
    margin-bottom: 16px;
}
.inp .rember{
     display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
}
.inp .rember p:first-of-type{
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
}
.inp .rember p:nth-of-type(2){
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
}

.inp .rember input{
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}

.inp .rember p span{
    display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
/*left: 20px;*/

}
#geetest{
	margin-top: 20px;
}
.login_btn{
     width: 100%;
    height: 45px;
    background: #84cc39;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
}
.inp .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
}
.inp .go_login span{
    color: #84cc39;
    cursor: pointer;
}
</style>
