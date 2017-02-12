// fis3 release -d output
// cd ./output
// cat ./style.css #view result

fis.match('*.css', {
  useHash: true, //default is `true`
  // compress css invoke fis-optimizer-clean-css
  packTo: '/output/js/all.css', 

  optimizer: fis.plugin('clean-css', {
    // option of clean-css
  })
});
// You need install it.
// npm i fis-optimizer-html-minifier [-g]
//
fis.match('*pages/.html', {
  //invoke fis-optimizer-html-minifier
  optimizer: fis.plugin('html-minifier')
});
fis.match('static/*.js', {
  useHash: true, // default is true
  // 指定压缩插件 fis-optimizer-uglify-js
   packTo: '/output/js/all.js', 
  optimizer: fis.plugin('uglify-js', {
    // option of uglify-js
  })
});
