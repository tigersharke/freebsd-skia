--- gyp/gpu.gyp.orig	2013-06-24 03:19:50.000000000 -0500
+++ gyp/gpu.gyp	2013-06-25 06:45:48.679671051 -0500
@@ -9,6 +9,10 @@
         'sources/': [ ['exclude', '_mac.(h|cpp|m|mm)$'],
         ],
       }],
+      [ 'skia_os != "freebsd"', {
+        'sources/': [ ['exclude', '_unix.(h|cpp)$'],
+        ],
+      }],
       ['skia_os != "linux" and skia_os != "chromeos"', {
         'sources/': [ ['exclude', '_unix.(h|cpp)$'],
         ],
@@ -40,6 +44,11 @@
           'GR_LINUX_BUILD=1',
         ],
       }],
+      [ 'skia_os == "freebsd"', {
+        'defines': [
+          'GR_LINUX_BUILD=1',
+        ],
+      }],
       [ 'skia_os == "ios"', {
         'defines': [
           'GR_IOS_BUILD=1',
@@ -93,7 +102,7 @@
             'GR_MAC_BUILD=1',
           ],
         }],
-        [ 'skia_os == "linux"', {
+        [ 'skia_os == "linux" or skia_os == "freebsd"', {
           'defines': [
             'GR_LINUX_BUILD=1',
           ],
@@ -132,16 +141,16 @@
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
@@ -177,6 +186,19 @@
             'GR_ANDROID_PATH_RENDERING=1',
           ],
         }],
+        [ 'skia_os == "freebsd"', {
+          'sources!': [
+            '../src/gpu/gl/GrGLDefaultInterface_none.cpp',
+            '../src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
+          ],
+          'link_settings': {
+            'libraries': [
+              '-lGL',
+              '-lGLU',
+              '-lX11',
+            ],
+          },
+        }],
         [ 'skia_os == "linux" or skia_os == "chromeos"', {
           'sources!': [
             '../src/gpu/gl/GrGLDefaultInterface_none.cpp',
@@ -197,6 +219,13 @@
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
         [ 'skia_mesa and skia_os == "linux"', {
           'link_settings': {
             'libraries': [
@@ -237,17 +266,17 @@
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
