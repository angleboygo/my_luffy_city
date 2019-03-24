<template>
  <div class="courselist">
    <div class="course-box">
      <el-row class="course-item">
        <el-col :span="12" class="course-item-left">
          <img src="../../assets/python21天入门.jpeg" alt>
        </el-col>
        <el-col :span="12" class="course-item-right">
          <div class="course-title">
            <span class="left">Python开发21天入门</span>
            <span class="right">30907人已加入学习</span>
          </div>
          <div class="course-author">
            <span class="left">Alex 金角大王 老男孩Python教学总监</span>
            <span class="right">共154课时/更新完成</span>
          </div>

          <el-row class="course-content">
            <el-col :span="12"><span><img src="../../assets/play.svg" alt="">01 | 常用模块学习-模块的种类和导入方法</span><i>免费</i></el-col>
            <el-col :span="12" class='offset'><span><img src="../../assets/play.svg" alt="">02 | 编程语言介绍（三）高级语言</span><i>免费</i></el-col>
            <el-col :span="12"><span><img src="../../assets/play.svg" alt="">03 | 三元运算</span><i>免费</i></el-col>
            <el-col :span="12" class='offset'><span><img src="../../assets/play.svg" alt="">04 | 编程语言介绍（一）</span><i>免费</i></el-col>
   
          </el-row>

          <div class="course-price">
            <span class='discount'>限时免费</span>
            <span class='present-price'>￥0.00元</span>
            <span class='original-price'>原价：9.00元</span>
            <button class='buy_now'>立即购买</button>
          </div>
          <div></div>
        </el-col>
      </el-row>
    </div>
        </div>
 
</template>

<script>
export default {
  name: "CourseList",
  data() {
    return {};
  }
};
</script>


<style  scoped>
.courselist {
  background-color: #f6f6f6;
}
.course-box {
  margin: auto;
  width: 1050px;
  height: auto;
  padding: 20px 30px 20px 20px;
  margin-bottom: 35px;
  transition: all 0.2s ease;
  border-radius: 2px;

  cursor: pointer;
  background: #fff;
  box-shadow: 2px 3px 16px rgba(0, 0, 0, 0.1);
}

.course-item-left {
  width: 423px;
  height: 210px;
  margin-right: 30px;
}
.course-item-left img {
  width: 100%;
  height: 100%;
  vertical-align: middle;
}
.course-title {
  width: 100%;
  line-height: 37px;
  margin-bottom: 8px;
}
.course-item-right {
  width: 596px;
  height: auto;
}
.course-item-right left {
  position: absolute;
  left: 0px;
}
.course-item-right .right {
  position: absolute;
  right: 0px;
}
.course-title .left {
  font-size: 26px;
  color: #333;
}
.course-title .right {
  font-size: 14px;
  color: #9b9b9b;
  font-family: PingFangSC-Light;
  position: absolute;
  right: 0px;
}

.course-author {
  font-size: 14px;
  color: #9b9b9b;
  margin-bottom: 14px;
  padding-bottom: 14px;
  font-family: PingFangSC-Light;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, 0.05);
}

.course-content {
  display: flex;
  flex-wrap: wrap;
  font-size: 14px;
  color: #666;
   

}

.course-content .el-col{
  width: 49%;
  margin-bottom: 15px;
  cursor: pointer;
  max-width: 227px;
   
}
.course-content img{
    width: 16px;
    height: 16px;
    line-height: 16px;
    margin-right: 6px;
    margin-bottom: 1.5px;
    vertical-align: middle;
    display: inline-block;
}
.course-content .el-col span{
   text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
    font-family: PingFangSC-Regular;
}

.course-content .el-col i{
    font-style:normal;
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
.course-content .offset{
  padding-left: 100px;
}
.course-price{
  height: 38px;
  line-height: 36px;
  margin-top:7px; 
  justify-items: center; 
}

.course-price .discount{
  height: 38px;
  line-height: 36px;
  padding: 6px 10px;
  font-size: 16px;
  text-align: center;
  margin-right: 8px;
  background: #fa6240;
  color: #fff;
  border-radius: 10px 0 10px 0;
  border: 1px solid #fa6240;


}

.course-price .present-price{
    font-size: 24px;
    line-height: 38px;
    height: 38px;
    color: #fa6240;

}
.course-price .original-price{
  font-family: PingFangSC-Regular;
    text-decoration: line-through;
    font-size: 14px;
    color: #9b9b9b;
    margin-left: 10px;
}
.course-price .buy_now{
    width: 120px;
    height: 38px;
    background: transparent;/*透明*/
    color: #fa6240;
    font-size: 16px;
    border: 1px solid #fd7b4d;
    border-radius: 3px;
    font-family: PingFangSC-Regular;
    transition: all .2s ease-in-out;
    position:absolute;
    right: 0px;
}

</style>
