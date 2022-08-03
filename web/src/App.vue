<template>
  <div id="app">
    <el-container>
      <el-aside width="180px">
        徐氏金融管理系统
          <ul></ul>
          <router-link to="/wencai">问财评分</router-link>
          <ul><router-link to="/city">城市列表</router-link></ul>
          <ul>菜单2</ul>
          <ul>菜单3</ul>
          <ul> </ul>
          <ul> </ul>
          <ul></ul>
          <ul></ul>
          <ul></ul>
          <ul></ul>
          <ul></ul>
          <ul>扑街</ul>
        </el-aside>
      
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <!-- <City>city component</City> -->
          <router-view>
          <Wencai>wencai page</Wencai>
          </router-view>
          <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
        </el-main>
        
      </el-container>
    </el-container>

    <router-view></router-view>
    
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import City from './components/City.vue'
import Wencai from './components/Wencai.vue'

export default {
  name: 'App',
  // components: {
  //   // HelloWorld,
  //   // City,
  //   // Wencai
  // }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.el-header, .el-footer {
    background-color: #FBFAFA;
    color: rgb(51, 51, 51);
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #336666;
    color: rgb(255, 255, 255);
    text-align: center;
    /* line-height: 200px; */
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    /* line-height: 160px; */
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
