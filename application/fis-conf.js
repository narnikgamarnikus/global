fis.config.set('project.include', ['pages/**', 'macros/**', 'static/**']);
fis.config.set('project.exclude', ['pages/**.less', 'macros/**.less', 'static/**.less', 'static/**/*.png', 'static/**/*.jpg', 'static/**/*.jpeg', 'static/**/*.ico']);
fis.config.set('modules.postpackager', 'simple');
fis.config.set('pack', {
    'pkg/libs.js': [
        'static/js/libs/jquery.min.js',
        'static/js/libs/bootstrap.min.js',
        'static/js/libs/respond.min.js',
        'static/js/init.js'
    ],
    'pkg/layout.js': [
        'static/js/layout.js',
        'static/output/macros.js'
    ],
    'pkg/libs.css': [
        'static/css/libs/*.css'
    ],
    'pkg/layout.css': [
        'static/css/bootstrap.theme.css',
        'static/css/common.css',
        'static/output/macros.css',
        'static/css/layout.css'
    ],
    'pkg/style.css': [
        'static/css/magnific-popup.css',
        'static/css/style.css',
        'static/css/colors/default.css'
    ],
    'pkg/style.js': [
        'static/js/libs/jquery.easing.1.3.min.js',
        'static/js/jquery.sticky.js',
        'static/js/libs/jquery.magnific-popup.min.js',
        'static/js/jquery.ajaxchimp.js',
        'static/js/jquery.app.js',
        'static/js/switcher.js'
    ]
});
