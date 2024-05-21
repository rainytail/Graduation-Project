module.exports = {
    publicPath: './',
    outputDir: 'dist',
    lintOnSave: true,
    runtimeCompiler: true, //关键点在这  
    // 调整内部的 webpack 配置。
    // 查阅 https://github.com/vuejs/vue-doc-zh-cn/vue-cli/webpack.md
    chainWebpack: () => {},
    configureWebpack: () => {},
}