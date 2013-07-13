--- gyp/gpu.gyp.orig	2013-07-11 04:16:54.000000000 -0500
+++ gyp/gpu.gyp	2013-07-13 05:08:44.382137150 -0500
@@ -9,7 +9,7 @@
         'sources/': [ ['exclude', '_mac.(h|cpp|m|mm)$'],
         ],
       }],
-      ['skia_os != "linux" and skia_os != "chromeos"', {
+      ['skia_os != "linux" and skia_os != "chromeos" and skia_os != "freebsd"', {
         'sources/': [ ['exclude', '_unix.(h|cpp)$'],
         ],
       }],
@@ -35,7 +35,7 @@
           'GR_MAC_BUILD=1',
         ],
       }],
-      [ 'skia_os == "linux" or skia_os == "chromeos"', {
+      [ 'skia_os == "linux" or skia_os == "chromeos" or skia_os == "freebsd"', {
         'defines': [
           'GR_LINUX_BUILD=1',
         ],
@@ -98,6 +98,11 @@
             'GR_LINUX_BUILD=1',
           ],
         }],
+        [ 'skia_os == "freebsd"', {
+          'defines': [
+            'GR_LINUX_BUILD=1',
+          ],
+        }],
         [ 'skia_os == "ios"', {
           'defines': [
             'GR_IOS_BUILD=1',
@@ -132,16 +137,16 @@
         '../include/gpu',
         '../src/gpu',
       ],
-      'dependencies': [
-        'angle.gyp:*',
-      ],
-      'export_dependent_settings': [
-        'angle.gyp:*',
-      ],
+#      'dependencies': [
+#        'angle.gyp:*',
+#      ],
+#      'export_dependent_settings': [
+#        'angle.gyp:*',
+#      ],
       'sources': [
         '<@(skgpu_sources)',
         '<@(skgpu_native_gl_sources)',
-        '<@(skgpu_angle_gl_sources)',
+#        '<@(skgpu_angle_gl_sources)',
         '<@(skgpu_mesa_gl_sources)',
         '<@(skgpu_debug_gl_sources)',
         '<@(skgpu_null_gl_sources)',
@@ -177,7 +182,7 @@
             'GR_ANDROID_PATH_RENDERING=1',
           ],
         }],
-        [ 'skia_os == "linux" or skia_os == "chromeos"', {
+        [ 'skia_os == "linux" or skia_os == "chromeos" or skia_os == "freebsd"', {
           'sources!': [
             '../src/gpu/gl/GrGLDefaultInterface_none.cpp',
             '../src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
@@ -204,6 +209,13 @@
             ],
           },
         }],
+        [ 'skia_mesa and skia_os == "freebsd"', {
+          'link_settings': {
+            'libraries': [
+              '-lOSMesa',
+            ],
+          },
+        }],
         [ 'skia_os == "mac"', {
           'link_settings': {
             'libraries': [
@@ -237,17 +249,17 @@
             '../src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
           ],
         }],
-        [ 'not skia_angle', {
-          'sources!': [
-            '<@(skgpu_angle_gl_sources)',
-          ],
-          'dependencies!': [
-            'angle.gyp:*',
-          ],
-          'export_dependent_settings!': [
-            'angle.gyp:*',
-          ],
-        }],
+#        [ 'not skia_angle', {
+#          'sources!': [
+#            '<@(skgpu_angle_gl_sources)',
+#          ],
+#          'dependencies!': [
+#            'angle.gyp:*',
+#          ],
+#          'export_dependent_settings!': [
+#            'angle.gyp:*',
+#          ],
+#        }],
         [ 'skia_os == "android"', {
           'sources!': [
             '../src/gpu/gl/GrGLDefaultInterface_none.cpp',
