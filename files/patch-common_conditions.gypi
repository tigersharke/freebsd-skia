--- gyp/common_conditions.gypi.orig	2013-07-24 21:29:26.000000000 -0500
+++ gyp/common_conditions.gypi	2013-07-24 23:58:59.032824719 -0500
@@ -210,11 +210,11 @@
           },
         },
         'cflags': [
-          '-Wall',
-          '-Wextra',
+#          '-Wall',
+#          '-Wextra',
           # suppressions below here were added for clang
           '-Wno-unused-parameter',
-          '-Wno-c++11-extensions'
+#          '-Wno-c++11-extensions'
         ],
         'conditions' : [
           [ 'skia_shared_lib', {
