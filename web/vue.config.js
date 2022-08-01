const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false  //关闭语法检查，放这里无效
})

module.exports = {
  devServer: {
      host: "0.0.0.0",  //指定要使用的 host
      port: 8001,   //指定端口号以侦听
      // hotOnly: false, //启用热模块替换，而无需页面刷新作为构建失败时的回退。
  },
  lintOnSave: false,  //关闭语法检查
};