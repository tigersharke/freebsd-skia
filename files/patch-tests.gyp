--- gyp/tests.gyp.orig	2013-07-13 06:20:54.732112277 -0500
+++ gyp/tests.gyp	2013-07-13 06:21:14.242108398 -0500
@@ -133,7 +133,7 @@
       'dependencies': [
         'skia_lib.gyp:skia_lib',
         'flags.gyp:flags',
-        'experimental.gyp:experimental',
+#        'experimental.gyp:experimental',
         'pdf.gyp:pdf',
         'tools.gyp:picture_utils',
       ],
