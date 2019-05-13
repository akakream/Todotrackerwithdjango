const { src, dest, series, parallel, watch } = require('gulp');
const merge = require('merge2');

// CSS
const sass = require('gulp-sass');
const minifyCSS = require('gulp-csso');
const concatCss = require('gulp-concat-css');
const autoprefixer = require('gulp-autoprefixer');
// JS
const minifyJS = require('gulp-uglify-es').default;
const concat = require('gulp-concat');


// handle css generation
function css() {
  return src('src/scss/*.scss')
    .pipe(sass({outputStyle: 'expanded'}))  // compile custom SCSS
    .pipe(concatCss('app.min.css'))         // concat into single file 
    .pipe(autoprefixer({
      browsers: ['last 2 versions'],
      cascade: false
    }))                                     // prefix file       
    .pipe(minifyCSS())                      // minify css
    .pipe(dest('todos/static/todos'))       // put file into to todos/static/todos
}


// handle js deployment
function js() {
  // load js files
  var jquery = src('node_modules/jquery/dist/jquery.min.js');
  var popper = src('node_modules/popper.js/dist/umd/popper.min.js');
  var bootstrap = src('node_modules/bootstrap/dist/js/bootstrap.min.js');

  var app = src('src/js/*.js')
    .pipe(minifyJS());                      // minify js
  
  return merge(jquery, popper, bootstrap, app)
    .pipe(concat('app.min.js'))             // concat all js files
    .pipe(dest('todos/static/todos'))       // put files into todos/static/todos
}

// static server and watching for filechanges
function serve() {
  // watch for changes
  watch('src/scss/*.scss', css);            // update css on filechange
  watch('src/js/*.js', js);                 // update js on filechange
}

// exports
exports.js = js;
exports.css = css;
exports.serve = serve;
exports.default = series(parallel(css, js), serve);