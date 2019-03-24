<template>
    <div class='home'>
        <Header/>
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

        }
    },
    components:{
        Header,
        Banner,
        Footer,
    }
}
</script>

<style scoped>
.body{
    margin: 0 auto;
    padding: 0 auto;
}

</style>
