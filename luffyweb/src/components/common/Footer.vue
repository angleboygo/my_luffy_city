<template>
  <el-footer height='128px'>
    <el-row classs="footer-1">
      <el-col :span="4">关于我们</el-col>
      <el-col :span="4">联系我们</el-col>
      <el-col :span="4">商务合作</el-col>
      <el-col :span="4">帮助中心</el-col>
      <el-col :span="4">意见反馈</el-col>
      <el-col :span="4">新手指南</el-col>
    </el-row>
    <el-row class="copyright">
      <el-col :span="24">Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</el-col>
    </el-row>
  </el-footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {};
  }
};
</script>


<style  scoped>
.el-footer{
  font-size: 14px;
  padding-top: 35px;
  color:white;
  text-align: center;
  background: #25292e;

}
.el-row{
  width: 850px;
  margin: 0 auto;
  padding-bottom: 26px;

}
.copyright{

  text-align: center;
  font-size: 12px;
}
</style>

