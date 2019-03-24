<template>
    <div class='cart'>
    <Header/>
    <div class='cart-content'>
        <div class='shopping-cart-tit'>我的购物车 <span>共2门课程</span></div>
        <table>
            <thead>
                <tr>
                    <td class="shopping-cart-list-head-item" width="8%" ></td>
                    <td class="shopping-cart-list-head-item" width="50%" >课程</td>
                    <td class="shopping-cart-list-head-item" width="20%" >有效期</td>
                    <td class="shopping-cart-list-head-item" width="15%" >单价</td>
                    <td class="shopping-cart-list-head-item" width="15%" >操作</td>
                </tr>
            </thead>
            <tbody>
               <tr>
                <td> <el-checkbox ></el-checkbox></td>
                <td>
                    <img src="../assets/Linux5周入门_1509589530.6144893.png" alt="">
                    <span>Linux系统基础5周入门精讲</span>
                </td>
                <td class='check-box'>
                   <el-select v-model="value" placeholder="请选择">
                        <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </td>
                <td>¥29.0</td>
                <td class='del'>删除</td>
               </tr>
               <tr>
                <td> <el-checkbox ></el-checkbox></td>
                <td>
                    <img src="../assets/Linux5周入门_1509589530.6144893.png" alt="">
                    <span>Linux系统基础5周入门精讲</span>
                </td>
                <td class='check-box'>
                   <el-select v-model="value" placeholder="请选择">
                        <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </td>
                <td>¥29.0</td>
                <td class='del'>删除</td>
               </tr>
               <tr>
                <td> <el-checkbox ></el-checkbox></td>
                <td>
                    <img src="../assets/Linux5周入门_1509589530.6144893.png" alt="">
                    <span>Linux系统基础5周入门精讲</span>
                </td>
                <td class='check-box'>
                   <el-select v-model="value" placeholder="请选择">
                        <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </td>
                <td>¥29.0</td>
                <td class='del'>删除</td>
               </tr>
               <tr>
                <td> <el-checkbox ></el-checkbox></td>
                <td>
                    <img src="../assets/Linux5周入门_1509589530.6144893.png" alt="">
                    <span>Linux系统基础5周入门精讲</span>
                </td>
                <td class='check-box'>
                   <el-select v-model="value" placeholder="请选择">
                        <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </td>
                <td>¥29.0</td>
                <td class='del'>删除</td>
               </tr>
               <tr>
                <td> <el-checkbox ></el-checkbox></td>
                <td>
                    <img src="../assets/Linux5周入门_1509589530.6144893.png" alt="">
                    <span>Linux系统基础5周入门精讲</span>
                </td>
                <td class='check-box'>
                   <el-select v-model="value" placeholder="请选择">
                        <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </td>
                <td>¥29.0</td>
                <td class='del'>删除</td>
               </tr>
             
            </tbody>
        </table>
    </div>

    <Footer/>
    </div>
</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
export default {
    name:'Cart',
    data() {
        return {
             options: [{
          value: '-1',
          label: '永久有效'
        }, {
          value: '30',
          label: '1个月'
        }, {
          value: '60',
          label: '2个月'
        }, {
          value: '90',
          label: '3个月'
        }],
        value:'-1',
            
        }
    },
    components: {
    Header,

    Footer,

  }
}
</script>

<style scoped>
.cart-content{
    margin: 0 auto;
    margin-top:80px;
    width: 1200px;  
    overflow: hidden; /*两个pindding造成浮动*/ 
}
.cart-content .shopping-cart-tit{

    font-size: 18px;
    color: #666;
    margin: 25px 0;
}
.cart-content .shopping-cart-tit span{
    font-size: 12px;
    color: #d0d0d0;
    display: inline-block;
}
table{
    font-size: 14px;
    width: 1200px;
    max-width: 100%;
    margin-bottom: 20px;
    text-align: left;

}
head{
  background: #F7F7F7;

}
thead tr{
    height: 80px;
    background: #F7F7F7;
    width: 100%;
   
}
td, th {
    display: table-cell;
    vertical-align: inherit;
}
tbody{
        display: table-row-group;
    vertical-align: middle;
    border-color: inherit;
}

tbody tr{
    color: aqua;
    border-bottom: 2px solid black;
    
}
table img{
    width: 175px;
    height: 115px;
    margin-right: 35px;
    vertical-align: middle;
}

tbody td{
    padding: 67px 10px;
    font-size: 16px;
    color: #333;
   
    border-bottom: 1px solid #ddd;
}

.del{
        color: #ffc210;
}
 
</style>
