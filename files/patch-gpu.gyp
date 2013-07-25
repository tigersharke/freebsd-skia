--- gyp/gpu.gyp.orig	2013-07-24 23:28:04.565741036 -0500
+++ gyp/gpu.gyp	2013-07-24 23:35:41.272195272 -0500
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
+      [ 'skia_os == "linux" or skia_os == "chromeos" and skia_os == "freebsd"', {
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
@@ -122,7 +127,7 @@
       'type': 'static_library',
       'standalone_static_library': 1,
       'dependencies': [
-        'angle.gyp:*',
+#        'angle.gyp:*',
         'core.gyp:*',
         'utils.gyp:*',
       ],
@@ -135,12 +140,12 @@
         '../src/gpu',
       ],
       'export_dependent_settings': [
-        'angle.gyp:*',
+#        'angle.gyp:*',
       ],
       'sources': [
         '<@(skgpu_sources)',
         '<@(skgpu_native_gl_sources)',
-        '<@(skgpu_angle_gl_sources)',
+#        '<@(skgpu_angle_gl_sources)',
         '<@(skgpu_mesa_gl_sources)',
         '<@(skgpu_debug_gl_sources)',
         '<@(skgpu_null_gl_sources)',
@@ -176,7 +181,7 @@
             'GR_ANDROID_PATH_RENDERING=1',
           ],
         }],
-        [ 'skia_os == "linux" or skia_os == "chromeos"', {
+        [ 'skia_os == "linux" or skia_os == "chromeos" or skia_os == "freebsd"', {
           'sources!': [
             '../src/gpu/gl/GrGLDefaultInterface_none.cpp',
             '../src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
@@ -203,6 +208,13 @@
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
@@ -236,17 +248,17 @@
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
