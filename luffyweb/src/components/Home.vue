<template>
    <div class='home' :current_page="current_page">
        <Header />
        <Banner/>
        <Footer/>  
    </div>
</template>


<script>

import Header from './common/Header'
import Banner from './common/Banner'
import Footer from './common/Footer'
export default {
    name:'Home',
    data() {
        return {
             current_page:0,
        };
    },
    components:{
        Header,
        Banner,
        Footer,
    },
}
</script>

<style scoped>
.body{
    margin: 0 auto;
    padding: 0 auto;
}

</style>
