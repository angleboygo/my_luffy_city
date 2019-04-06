<template>
	<div class="box">
		<img src="https://www.luffycity.com/static/img/Loginbg.3377d0c.jpg" alt="">
		<div class="register">
			<div class="register_box">
        <div class="register-title">注册路飞学城</div>
				<div class="inp">
          <!-- <el-select v-model="region">
            <el-option v-for="item in region_list" :label="item.nation_name+'('+item.nation_code+')'" :value="item.nation_code"></el-option>
          </el-select> -->
					<input v-model = "mobile" type="text" placeholder="手机号码" class="user">
					<input v-model = "password" type="password" placeholder="密码" class="user">
					<input v-model = "password2" type="password" placeholder="确认密码" class="user">
          <div id="geetest"></div>
					<div class="sms">
            <input v-model="sms_code" maxlength="16" type="text" placeholder="输入验证码" class="user">
            <span class="get_sms" @click="send_sms">{{get_sms_text}}</span>
          </div>
					<button class="register_btn" @click="registerHander">注册</button>
					<p class="go_login" >已有账号 <router-link to="/login">直接登录</router-link></p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
  name: 'Register',
  data(){
    return {
        region:"+86",
        sms_code:"",
        password:"",
        password2:"",
        mobile:"",
        validateResult:false,
        get_sms_text:"获取验证码",
    }
  },
  created(){
    // 页面初始化的时候设置号码的地区号
    // this.region_list = nation; //nation为nation.js中的变量名


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
              width: "350px",
              product: "embed", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
              offline: !data.success // 表示用户后台检测极验服务器是否宕机，一般不需要关注
              // 更多配置参数请参见：http://www.geetest.com/install/sections/idx-client-sdk.html#config
          }, this.handlerPopup);
    }).catch(error=>{
      console.log(error)
    })

  },
  methods:{
    send_sms(){
      let reg = /1[1-9]{2}\d{8}/;
      if( !reg.test(this.mobile) ){
        return false;
      }

      // 如果get_sms_text 不是文本,而是数字,则表示当前手机号码还在60秒的发送短信间隔内
      if(this.get_sms_text != "获取验证码"){
        return false;
      }

      // 发送短信
      let _this = this;
      this.$axios.get("http://127.0.0.1:8000/users/sms/?mobile="+this.mobile).then(response=>{
        console.log(response);
        // 显示发送短信以后的文本倒计时
        let time = 60;
        let timer = setInterval(()=>{
          --time;
          if(time <=1){
            // 如果倒计时为0,则关闭当前定时器
             _this.get_sms_text = "获取验证码";
            clearInterval(timer);
          }else{
              _this.get_sms_text = time;
          }
        },1000)
      }).catch(error=>{
        console.log(error);
      })

    },
    registerHander(){
      // 注册信息提交
      // 提交数据前判断用户是否通过了验证码校验
      if(!this.validateResult){
          alert("验证码验证有误");
          return false;
      }

      this.$axios.post("http://127.0.0.1:8000/users/user/",{
          
          "mobile":this.mobile,
          "password":this.password,
          "password2":this.password2,
          "sms_code":this.sms_code,
        },{
          responseType:"json",
        }).
          then(response=>{
             console.log(this.validateResult);
            // 请求成功，保存登陆状态
            localStorage.removeItem("token");
            let data = response.data;
            sessionStorage.token = data.token;
            sessionStorage.id = data.id;
            sessionStorage.username = data.mobile;
            // 注册成功以后默认表示已经登录了,跳转用户中心的页面
            this.$router.push("/user");
            // alert("注册成功!");
        }).catch(error=>{
           console.log(this.validateResult);
            alert("注册失败!");
            // error 就是一个对象,里面会保存在错误响应时的http状态码以及后端抛出的错误信息
        })
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

};
</script>

<style scoped>
.box{
	width: 100%;
  height: 100%;
	position: relative;
  overflow: hidden;
}
.el-select{
  width:100%;
  margin-bottom: 15px;
}
.box img{
	width: 100%;
  min-height: 100%;
}
.box .register {
	position: absolute;
	width: 500px;
	height: 400px;
	top: 0;
	left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}
.register .register-title{
    width: 100%;
    font-size: 24px;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #4a4a4a;
    letter-spacing: .39px;
}
.register-title img{
    width: 190px;
    height: auto;
}
.register-title p{
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
}
.sms{
  margin-top: 15px;
  position: relative;
}
.sms .get_sms{
  position: absolute;
  right: 15px;
  top: 14px;
  font-size: 14px;
  color: #ffc210;
  cursor: pointer;
  border-left: 1px solid #979797;
  padding-left: 20px;
}

.register_box{
    width: 400px;
    height: auto;
    background: #fff;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
}
.register_box .title{
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
.register_box .title span:nth-of-type(1){
	color: #4a4a4a;
    	border-bottom: 2px solid #84cc39;
}

.inp{
	width: 350px;
	margin: 0 auto;
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

}
#geetest{
	margin-top: 20px;
}
.register_btn{
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
