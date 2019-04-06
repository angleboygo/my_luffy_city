<template>
  <div class="banner">
         <!-- <span class="demonstration">Click 指示器触发</span> -->
    <el-carousel trigger="click" height="687.38px" >
      <el-carousel-item v-for="item,tt in banner_list" :key="tt">
        <a href="item.link"><img :src="item.image" alt=""></a>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
        banner_list:[]
    };
  },
    created: function(){
      console.log(this.$axios);
      // 获取轮播图
 this.$axios.get("http://api.luffycity.cn:8000/home/banner/").then(res => {
        this.banner_list = res.data;
      }).catch(error => {
        console.log(error);
      });
  }
};
</script>


<style scoped>


.banner img{
  width: 100%;
}
.el-carousel__indicator{
        cursor: pointer;
        border: 1px solid #fff;
}

 </style> 
