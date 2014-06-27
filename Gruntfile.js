var path = require('path');
function createDjangoStaticConcatConfig(context, block) {
  'use strict';
  var cfg = {files: []};
  var staticPattern = /\{\{\s*STATIC_URL\s*\}\}/;

  block.dest = block.dest.replace(staticPattern, '');
  var outfile = path.join(context.outDir, block.dest);

  // Depending whether or not we're the last of the step we're not going to output the same thing
  var files = {
    dest: outfile,
    src: []
  };
  context.inFiles.forEach(function (f) {
    files.src.push(path.join(context.inDir, f.replace(staticPattern, '')));
  });
  cfg.files.push(files);
  context.outFiles = [block.dest];
  return cfg;
}


module.exports = function (grunt) {
  'use strict';
  // Load grunt tasks automatically
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take. Can help when optimizing build times
  require('time-grunt')(grunt);

  grunt.initConfig({


    pkg: grunt.file.readJSON('package.json'),
    stringulator: {
      root: 'stringulator',
      static: 'stringulator/static',
      dist: 'dist',
      templates: 'stringulator/templates'
    },
    // add a preprocessor to modify the concat config to parse out {{STATIC_URL}} using the above method
    useminPrepare: {
      html: 'stringulator/templates/base.html',
      options: {
        dest: 'dist',
        flow: {
          steps: {
            js: [
              {
                name: 'concat',
                createConfig: createDjangoStaticConcatConfig
              },
              'uglifyjs'
            ],
            // also apply it to css files
            css: [
              {
                name: 'cssmin',
                createConfig: createDjangoStaticConcatConfig
              }
            ]
          },
          // this property is necessary
          post: {}
        }
      }
    },

    // add a pattern to parse out the actual filename and remove the {{STATIC_URL}} bit
    usemin: {
      html: ['dist/{,*/}*.html'],
      css: ['dist/styles/{,*/}*.css'],
      options: {
        assetsDirs: ['dist'],
        patterns: {
          html: [
            [/\{\{\s*STATIC_URL\s*\}\}([^'"]*)["']/mg, 'django static']
          ]
        }
      }
    },

    // Empties folders to start fresh
    clean: {
      dist: {
        files: [
          {
            dot: true,
            src: [
              '.tmp',
              '<%= stringulator.dist %>/{,*/}*',
              '!<%= stringulator.dist %>/.git*'
            ]
          }
        ]
      }
    },
    concat: {
      options: {
        separator: ';'
      },
      dist: {
        src: ['<%= stringulator.static %>/js/**/*.js'],
        dest: '<%= stringulator.dist %>/static/js/vendor.js'
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          '<%= stringulator.dist %>/static/js/vendor.min.js': ['<%= stringulator.dist %>/static/js/vendor.js']
        }
      }
    },
    // Copies remaining files to places other tasks can use
    copy: {
      dist: {
        files: [
          {
            expand: true,
            dot: true,
//          cwd: '<%= stringulator.root %>',
            dest: '<%= stringulator.dist %>',
            src: [
//            '*.{ico,png,txt}',
//            '*.html',
//              '<%= stringulator.templates %>/**/{,*/}*.html'
//            'images/{,*/}*.{webp}',
//            'fonts/*'
            ]
          }
        ]
      }
    },

    jshint: {
      options: {
        jshintrc: '.jshintrc',
        reporter: require('jshint-stylish')
      },
      all: {
        src: [
          'Gruntfile.js',
          '<%= stringulator.static %>/scripts/{,*/}*.js'
        ]
      },
      test: {
        src: ['test/spec/{,*/}*.js']
      }
    },
    cssmin: {
      dist: {
        files: {
          '<%= stringulator.dist %>/static/stylesheets/main.css': [
            '<%= stringulator.static %>/stylesheets/**/{,*/}*.css'
          ]
        }
      }
    },
//    uglify: {
//      dist: {
//        files: {
//          '<%= yeoman.dist %>/scripts/scripts.js': [
//            '<%= yeoman.dist %>/scripts/scripts.js'
//          ]
//        }
//      }
//    }
//    concat: {
//      dist: {}
//    }

    /*jshint camelcase: false */
    aws_s33: {
      options: {
        accessKeyId: '<%= aws.AWSAccessKeyId %>', // Use the variables
        secretAccessKey: '<%= aws.AWSSecretKey %>', // You can also use env variables
        region: 'eu-west-1',
        uploadConcurrency: 5, // 5 simultaneous uploads
        downloadConcurrency: 5 // 5 simultaneous downloads
      },
      staging: {
        options: {
          bucket: 'my-wonderful-staging-bucket',
          differential: true // Only uploads the files that have changed
        },
        files: [
          {dest: 'app/', cwd: 'backup/staging/', action: 'download'},
          {expand: true, cwd: 'dist/staging/scripts/', src: ['**'], dest: 'app/scripts/'},
          {expand: true, cwd: 'dist/staging/styles/', src: ['**'], dest: 'app/styles/'},
          {dest: 'src/app', action: 'delete'},
        ]
      },
//      production: {
//        options: {
//          bucket: 'my-wonderful-production-bucket'
//          params: {
//            ContentEncoding: 'gzip' // applies to all the files!
//          }
//          mime: {
//            'dist/assets/production/LICENCE': 'text/plain'
//          }
//        },
//        files: [
//          {expand: true, cwd: 'dist/production/', src: ['**'], dest: 'app/'},
//          {expand: true, cwd: 'assets/prod/large', src: ['**'], dest: 'assets/large/', stream: true}, // enable stream to allow large files
//          {expand: true, cwd: 'assets/prod/', src: ['**'], dest: 'assets/', params: {CacheControl: '2000'},
//          // CacheControl only applied to the assets folder
//          // LICENCE inside that folder will have ContentType equal to 'text/plain'
//        ]
//      },
      cleanProduction: {
        options: {
          bucket: 'my-wonderful-production-bucket',
          debug: true // Doesn't actually delete but shows log
        },
        files: [
          {dest: 'app/', action: 'delete'},
          {dest: 'assets/', exclude: '**/*.tgz', action: 'delete'}, // will not delete the tgz
          {dest: 'assets/large/', exclude: '**/*copy*', flipExclude: true, action: 'delete'}, // will delete everything that has copy in the name
        ]
      },
      downloadProduction: {
        options: {
          bucket: 'my-wonderful-production-bucket'
        },
        files: [
          {dest: 'app/', cwd: 'backup/', action: 'download'}, // Downloads the content of app/ to backup/
          {dest: 'assets/', cwd: 'backup-assets/', exclude: '**/*copy*', action: 'download'}, // Downloads everything which doesn't have copy in the name
        ]
      },
      secret: {
        options: {
          bucket: 'my-wonderful-private-bucket',
          access: 'private'
        },
        files: [
          {expand: true, cwd: 'secret_garden/', src: ['*.key'], dest: 'secret/'},
        ]
      }
    }
  });


  grunt.registerTask('test', ['jshint']);

  grunt.registerTask('build', [
    'jshint',
    'clean',
//    'wiredep',
//    'useminPrepare',
    'concat',
//    'uglify',

//    'copy',
    'uglify',
    'cssmin',
//    'usemin'
  ]);

  grunt.registerTask('deploy-static', [
    'test',
    'build',
    'aws_s3'
  ]);

  grunt.registerTask('default', [
    'newer:jshint',
    'test',
    'build'
  ]);
};

