<template>
  <div class="large_box">
    <div class="main">
      <div class="filter">
        <el-row class="filter-el-row1">
          <el-col :span="2" class="filter-type">课程分类:</el-col>
          <el-col :span="2" class="current">全部</el-col>
          <el-col :span="2">Python</el-col>
          <el-col :span="3">Linux运维</el-col>
          <el-col :span="3">Python进阶</el-col>
          <el-col :span="3">开发工具</el-col>
          <el-col :span="2">Go语言</el-col>
          <el-col :span="2">机器学习</el-col>
          <el-col :span="3">技术生涯</el-col>
        </el-row>
        <el-row class="filter-el-row2">
          <el-col :span="2" class="filter-type">筛&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选:</el-col>
          <el-col :span="2" >默认</el-col>
          <el-col :span="2">人气</el-col>
          <el-col :span="3">
            <span @click.stop='filter_price_condition=!filter_price_condition'  class='current'>价格</span>
            <div class="filter-price">
              <span class="ico-top" @click.stop='filter_price_condition=True' :class="filter_price_condition==true?'current':''">
                <i class="el-icon-caret-top"  ></i>
              </span>
              <span class="ico-bottom" @click.stop='filter_price_condition=false' :class="filter_price_condition==false?'current':''">
                <i class="el-icon-caret-bottom"></i>
              </span>
            </div>
          </el-col>
          <el-col :span="3" class="total">共2个课程</el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FilterCourse",
  data() {
    return {
      filter_price_condition:false,
    };
  }
};
</script>


<style  scoped>
.large_box {
  flex: 1;
  width: 100%;
  height: 100%;
  background: #f6f6f6;
  display: flex;
  align-items: flex-start;
}
.main {
  width: 1100px;
  height: auto;
  margin: 0 auto;
  padding-top: 35px;
}
.main .filter {
  text-align: center;
  width: 1050px;
  height: auto;
  margin-bottom: 35px;
  padding: 25px 30px 25px 20px;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px 0 #f0f0f0;
}
.main .filter-el-row1 {
  line-height: 30px;
  border-bottom: 1px solid #333;
  border-bottom-color: rgba(51, 51, 51, 0.05);
  padding-bottom: 18px;
  margin-bottom: 17px;
  align-items: center;
  font-size: 16px;
}

.main .filter-el-row2 {
  line-height: 28px;
  display: flex;
  align-items: center;
}
.filter-type {
  text-align: center;
}

.filter .filter-el-row1 .current {
  color: #ffc210;
  border: 1px solid #ffc210 !important;
  border-radius: 30px;
}
.filter .filter-el-row2 .current {
  color: #ffc210;
}
.filter .total {
  font-family: PingFangSC-Light;
  font-size: 14px;
  color: #9b9b9b;
  position: absolute;
  right: 0;
}

.filter .filter-price {
  display: inline-block;
  vertical-align: middle;
}

.filter .ico-top,
.filter .ico-bottom {
  display: block;
  color: #d8d8d8;
  line-height: 8px;
  margin: -4px;
  font-size: 13px;
}
</style>
