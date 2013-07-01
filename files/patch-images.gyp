--- gyp/images.gyp.orig	2013-06-25 07:47:17.759703639 -0500
+++ gyp/images.gyp	2013-06-25 07:48:46.199703625 -0500
@@ -8,7 +8,7 @@
       'standalone_static_library': 1,
       'dependencies': [
         'libjpeg.gyp:*',
-        'libwebp.gyp:libwebp',
+#        'libwebp.gyp:libwebp',
         'utils.gyp:utils',
       ],
       'export_dependent_settings': [
@@ -49,7 +49,7 @@
         '../src/images/SkImageDecoder_libico.cpp',
         '../src/images/SkImageDecoder_libjpeg.cpp',
         '../src/images/SkImageDecoder_libpng.cpp',
-        '../src/images/SkImageDecoder_libwebp.cpp',
+#        '../src/images/SkImageDecoder_libwebp.cpp',
         '../src/images/SkImageDecoder_wbmp.cpp',
         '../src/images/SkImageEncoder.cpp',
         '../src/images/SkImageEncoder_Factory.cpp',
