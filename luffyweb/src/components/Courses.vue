<template>
  <div class="courses">
      <Header :current_page="current_page"/>
      <div class="main">
          <div class="filter">
            <el-row class="filter-el-row1">
              <el-col :span="2" class="filter-text">课程分类:</el-col>
              <el-col :span="2" class="current">全部</el-col>
              <el-col :span="2">Python</el-col>
              <el-col :span="2">Linux运维</el-col>
              <el-col :span="2">Python进阶</el-col>
              <el-col :span="2">开发工具</el-col>
              <el-col :span="2">Go语言</el-col>
              <el-col :span="2">机器学习</el-col>
              <el-col :span="2">技术生涯</el-col>
            </el-row>
            <el-row class="filter-el-row2">
              <el-col :span="2" class="filter-text filter-text2">筛&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选:</el-col>
              <el-col :span="2" class="current">默认</el-col>
              <el-col :span="2">人气</el-col>
              <el-col :span="2" class="">
                <span @click.stop="filter_price=!filter_price">价格</span>
                <div class="filter-price">
                  <span class="up" @click.stop="filter_price=true" :class="filter_price==true?'active':''"><i class="el-icon-caret-top"></i></span>
                  <span class="down" @click.stop="filter_price=false"  :class="filter_price==false?'active':''"><i class="el-icon-caret-bottom"></i></span>
                </div>
              </el-col>
            </el-row>
          </div>
          <div class="courses_list">
              <el-row class="course-item">
                <el-col :span="24" class="course-item-box">
                  <el-row>
                    <el-col :span="12" class="course-item-left"><img src="/static/courses/675076.jpeg" alt=""></el-col>
                    <el-col :span="12" class="course-item-right">
                        <div class="course-title">
                          <p class="box-title">Go编程33天从入门到放弃系列</p>
                          <p class="box-number">30074人已加入学习</p>
                        </div>
                        <div class="author">
                          <p class="box-author">Alex 金角大王 老男孩Python教学总监</p>
                          <p class="lession">共154课时<span>/更新完成</span></p>
                        </div>
                        <el-row class="course-content">
                            <el-col :span="12"><i class="el-icon-caret-right"></i>01 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>02 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>03 | 三元运算符... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>04 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                        </el-row>
                        <div class="course-price">
                            <p class="course-price-left">
                              <span class="discount">限时免费</span>
                              <span class="count">¥0.00</span>
                              <span class="old_count">原价: ¥8.00元</span>
                            </p>
                            <button class="buy">立即购买</button>
                        </div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
              <el-row class="course-item">
                <el-col :span="24" class="course-item-box">
                  <el-row>
                    <el-col :span="12" class="course-item-left"><img src="/static/courses/675076.jpeg" alt=""></el-col>
                    <el-col :span="12" class="course-item-right">
                        <div class="course-title">
                          <p class="box-title">Go编程33天从入门到放弃系列</p>
                          <p class="box-number">30074人已加入学习</p>
                        </div>
                        <div class="author">
                          <p class="box-author">Alex 金角大王 老男孩Python教学总监</p>
                          <p class="lession">共154课时<span>/更新完成</span></p>
                        </div>
                        <el-row class="course-content">
                            <el-col :span="12"><i class="el-icon-caret-right"></i>01 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>02 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>03 | 三元运算符... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>04 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                        </el-row>
                        <div class="course-price">
                            <p class="course-price-left">
                              <span class="discount">限时免费</span>
                              <span class="count">¥0.00</span>
                              <span class="old_count">原价: ¥8.00元</span>
                            </p>
                            <button class="buy">立即购买</button>
                        </div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
              <el-row class="course-item">
                <el-col :span="24" class="course-item-box">
                  <el-row>
                    <el-col :span="12" class="course-item-left"><img src="/static/courses/675076.jpeg" alt=""></el-col>
                    <el-col :span="12" class="course-item-right">
                        <div class="course-title">
                          <p class="box-title">Go编程33天从入门到放弃系列</p>
                          <p class="box-number">30074人已加入学习</p>
                        </div>
                        <div class="author">
                          <p class="box-author">Alex 金角大王 老男孩Python教学总监</p>
                          <p class="lession">共154课时<span>/更新完成</span></p>
                        </div>
                        <el-row class="course-content">
                            <el-col :span="12"><i class="el-icon-caret-right"></i>01 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>02 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>03 | 三元运算符... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>04 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                        </el-row>
                        <div class="course-price">
                            <p class="course-price-left">
                              <span class="discount">限时免费</span>
                              <span class="count">¥0.00</span>
                              <span class="old_count">原价: ¥8.00元</span>
                            </p>
                            <button class="buy">立即购买</button>
                        </div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
              <el-row class="course-item">
                <el-col :span="24" class="course-item-box">
                  <el-row>
                    <el-col :span="12" class="course-item-left"><img src="/static/courses/675076.jpeg" alt=""></el-col>
                    <el-col :span="12" class="course-item-right">
                        <div class="course-title">
                          <p class="box-title">Go编程33天从入门到放弃系列</p>
                          <p class="box-number">30074人已加入学习</p>
                        </div>
                        <div class="author">
                          <p class="box-author">Alex 金角大王 老男孩Python教学总监</p>
                          <p class="lession">共154课时<span>/更新完成</span></p>
                        </div>
                        <el-row class="course-content">
                            <el-col :span="12"><i class="el-icon-caret-right"></i>01 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>02 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>03 | 三元运算符... <span class="free">免费</span> </el-col>
                            <el-col :span="12"><i class="el-icon-caret-right"></i>04 | 常用模块学习-模块的种类和... <span class="free">免费</span> </el-col>
                        </el-row>
                        <div class="course-price">
                            <p class="course-price-left">
                              <span class="discount">限时免费</span>
                              <span class="count">¥0.00</span>
                              <span class="old_count">原价: ¥8.00元</span>
                            </p>
                            <button class="buy">立即购买</button>
                        </div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
          </div>
      </div>
      <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"
  export default {
    name:"Courses",
    data(){
      return {
        current_page:1,
        filter_price:false,
      }
    },
    components:{
      Header,
      Footer,
    },
    methods:{
    }
  }
</script>


<style scoped>
.courses{
  padding-top: 80px;
}
.main{
    width: 1100px;
    height: auto;
    margin: 0 auto;
    padding-top: 35px;
}
.main .filter{
    width: 100%;
    height: auto;
    margin-bottom: 35px;
    padding: 25px 0px 25px 0px;
    background: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 4px 0 #f0f0f0;
}
.filter .el-col{
  text-align: center;
  padding: 6px 0px;
  line-height: 16px;
  margin-left: 14px;
  position: relative;
  transition: all .3s ease;
  cursor: pointer;
  color: #4a4a4a;
}
.filter-el-row1{
  padding-bottom: 18px;
  margin-bottom: 17px;
}
.filter .filter-text{
  text-align: right;
  font-size: 16px;
  color: #888;
}
.filter .filter-text2{
}
.filter .filter-el-row1 .current{
    color: #ffc210;
    border: 1px solid #ffc210!important;
    border-radius: 30px;
}
.filter .filter-el-row2 .current{
    color: #ffc210;
}
.filter-price{
  display:inline-block;
  vertical-align: middle;
}
.filter-price .up, .filter-price .down{
  display: block;
  line-height: 8px;
  font-size: 13px;
  margin: -4px;
  color: #d8d8d8;
}
.current .filter-price .active{
  color: #ffc210;
}
.course-item{
  margin-bottom: 35px;
}
.course-item .course-item-box{
   padding: 20px 30px 20px 20px;
}
.course-item{
     box-shadow: 2px 3px 16px rgba(0,0,0,.1);
    transition: all .2s ease;
}
.course-item .course-item-left{
    width: 423px;
    height: 210px;
    margin-right: 30px;
}
.course-title{
  overflow: hidden;/* 在父元素中使用可以清除子元素的浮动影响 */
}
.course-title .box-title{
  font-size: 26px;
  color: #333333;
  float: left;
  margin-bottom: 8px;
}
.course-title .box-number{
    font-size: 14px;
    color: #9b9b9b;
    font-family: PingFangSC-Light;
    float: right;
    padding-top: 12px;
}
.course-item-right{
  width: 56.6%;
}
.author{
    font-size: 14px;
    color: #9b9b9b;
    margin-bottom: 14px;
    padding-bottom: 14px;
    overflow: hidden;
}
.author .box-author{
  float:left;
}
.author .lession{
  float: right;
}
.course-content .el-icon-caret-right{
  border: 1px solid #000;
  border-radius: 50%;
  margin-right: 6px;
}
.course-content .el-col{
  font-size: 14px;
  color: #666;
  width: 50%;
  margin-bottom: 15px;
  cursor: pointer;
}
.course-content .el-col:hover{
  color: #ffc210;
}
.course-content .el-col:hover .el-icon-caret-right,.course-content .el-col:hover .free{
  border-color: #ffc210;
  color: #ffc210;
}
.course-content .el-col .free{
    width: 34px;
    height: 20px;
    color: #fd7b4d;
    margin-left: 10px;
    border: 1px solid #fd7b4d;
    border-radius: 2px;
    text-align: center;
    font-size: 13px;
    white-space: nowrap;
}
.course-price{
  overflow: hidden;
}
.course-price .course-price-left{
  float: left;
}
.course-price .discount{
    padding: 6px 10px;
    display: inline-block;
    font-size: 16px;
    color: #fff;
    text-align: center;
    margin-right: 8px;
    background: #fa6240;
    border: 1px solid #fa6240;
    border-radius: 10px 0 10px 0;
}
.course-price .course-price-left{
  line-height: 22px;
}
.course-price .count{
    font-size: 24px;
    color: #fa6240;
}
.course-price .old_count{
    font-size: 14px;
    color: #9b9b9b;
    text-decoration: line-through;
    margin-left: 10px;
}
.course-price .buy{
  float: right;
  width: 120px;
  height: 38px;
  font-size: 16px;
  border-radius: 3px;
  border: 1px solid #fd7b4d;
  background: transparent;/* 透明 */
  color: #fa6240;
  cursor: pointer;
  transition: all .2s ease-in-out;/* css3新版本的样式中支持支持 jQuery里面的动画预设效果 */
  /* all表示当前元素的所有样式  .2s表示改变样式完成的时间  ease-in-out */
}
.course-price .buy:hover{
    color: #fff;
    background: #ffc210;
    border: 1px solid #ffc210;
}
</style>
