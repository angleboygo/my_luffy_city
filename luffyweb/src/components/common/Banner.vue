<template>
  <div class="banner">
         <!-- <span class="demonstration">Click 指示器触发</span> -->
    <el-carousel trigger="click" height="687.38px" >
      <el-carousel-item v-for="item in img_list" :key="item">
        <img :src="item" alt="">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
        img_list:[
            "/static/banner/1.jpeg",
            "/static/banner/2.png",
            "/static/banner/3.png",
            "/static/banner/4.png",
            "/static/banner/5.png",
            "/static/banner/6.png",
        ]
    };
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
