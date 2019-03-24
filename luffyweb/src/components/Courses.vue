<template>
  <div class="courses">
    <Header/>
    <FilterCourse/>
    <CourseList/>
    <CourseList/>
    <CourseList/>
    <CourseList/>
    <Footer/>
  </div>
</template>


<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
import FilterCourse from "./courses/FilterCourse";
import CourseList from "./courses/CourseList";
export default {
  name: "Courses",
  data() {
    return {};
  },
  components: {
    Header,
    FilterCourse,
    Footer,
    CourseList,
  }
};
</script>

<style scoped>
.courses {
  padding-top: 80px;
}
</style>
