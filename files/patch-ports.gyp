--- gyp/ports.gyp.orig	2013-07-24 21:29:26.000000000 -0500
+++ gyp/ports.gyp	2013-07-25 04:01:20.075698836 -0500
@@ -53,7 +53,7 @@
             'freetype.gyp:freetype',
           ],
         }],
-        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris", "chromeos"]', {
+        [ 'skia_os in ["linux", "openbsd", "solaris", "chromeos"]', {
           'link_settings': {
             'libraries': [
               '-lfontconfig',
@@ -66,6 +66,19 @@
             '../src/ports/SkFontConfigInterface_direct.cpp',
           ],
         }],
+        [ 'skia_os == "freebsd"', {
+          'link_settings': {
+            'libraries': [
+              '-lfontconfig',
+              '-lc',
+            ],
+          },
+          'sources': [
+            '../src/fonts/SkFontMgr_fontconfig.cpp',
+            '../src/ports/SkFontHost_fontconfig.cpp',
+            '../src/ports/SkFontConfigInterface_direct.cpp',
+          ],
+        }],
         [ 'skia_os == "nacl"', {
           'sources': [
             '../src/ports/SkFontHost_linux.cpp',
