var gulp = require('gulp');
var path = require('path');
var less = require('gulp-less');
var concat = require('gulp-concat');
var watch = require('gulp-watch');
var batch = require('gulp-batch');
var plumber = require('gulp-plumber');
var header = require('gulp-header');
var footer = require('gulp-footer');
var rename = require("gulp-rename");
var image = require("gulp-image");
var changed = require('gulp-changed');
var fontgen = require('gulp-fontgen');
 
gulp.task('fontgen', function() {
  return gulp
  .src(path.join(root, './static/fonts/*.{ttf,otf}'))
  .pipe(fontgen())
  .pipe(gulp.dest('output/static/fonts/'));
});

var root = './application';

gulp.task('macros-css', function () {
    return gulp
        .src(path.join(root, 'macros/**/_*.less'))
        .pipe(plumber())
        .pipe(less({
            paths: [path.join(root, 'static/css')]
        }))
        .pipe(concat('macros.css'))
        .pipe(gulp.dest(path.join(root, 'static/output/')));
});

gulp.task('styles-css', function () {
    return gulp
        .src(path.join(root, 'static/css/_*.css'))
        .pipe(plumber())
        .pipe(concat('macros.css'))
        .pipe(gulp.dest(path.join(root, 'static/output/')));
});

gulp.task('macros-js', function () {
    return gulp
        .src(path.join(root, 'macros/**/_*.js'))
        .pipe(plumber())
        .pipe(header('(function () {'))
        .pipe(footer('})();'))
        .pipe(concat('macros.js')
)        .pipe(gulp.dest(path.join(root, 'static/output/')));
});

gulp.task('pages-css', function () {
    return gulp
        .src(path.join(root, 'pages/**/*.less'))
        .pipe(plumber())
        .pipe(less({
            paths: [path.join(root, 'static/css')]
        }))
        .pipe(rename(function (path) {
            path.extname = ".css";
            return path;
        }))
        .pipe(gulp.dest(path.join(root, 'pages')));
});

gulp.task('global-css', function () {
    return gulp
        .src(path.join(root, 'static/css/**/*.less'))
        .pipe(plumber())
        .pipe(less({
            paths: [path.join(root, 'static/css')]
        }))
        .pipe(rename(function (path) {
            path.extname = ".css";
            return path;
        }))
        .pipe(gulp.dest(path.join(root, 'static/css')));
});

gulp.task('image', function () {
    return gulp
    .src(path.join(root, 'static/images/**/*'))
    .pipe(changed('./output/static/images', {hasChanged: changed.compareSha1Digest}))
    .pipe(image({
        pngquant: true,
        optipng: false,
        zopflipng: true,
        jpegRecompress: false,
        jpegoptim: true,
        mozjpeg: true,
        gifsicle: true,
        svgo: true,
        concurrent: 10
    }))
  .pipe(gulp.dest('./output/static/images'));
});


gulp.task('build', ['macros-css', 'macros-js', 'pages-css', 'global-css', 'image']);

gulp.task('watch', ['build'], function () {
    watch(path.join(root, 'macros/**/_*.js'), batch(function (events, done) {
        gulp.start('macros-js', done);
    }));
    watch(path.join(root, 'macros/**/_*.less'), batch(function (events, done) {
        gulp.start('macros-css', done);
    }));
    watch(path.join(root, 'pages/**/*.less'), batch(function (events, done) {
        gulp.start('pages-css', done);
    }));
    watch(path.join(root, 'static/css/**/*.less'), batch(function (events, done) {
        gulp.start('global-css', done);
    }));
});

gulp.task('default', ['build']);
