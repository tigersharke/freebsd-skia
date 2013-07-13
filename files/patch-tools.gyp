--- gyp/tools.gyp.orig	2013-07-11 04:16:54.000000000 -0500
+++ gyp/tools.gyp	2013-07-13 06:24:16.562110567 -0500
@@ -101,8 +101,8 @@
       'dependencies': [
         'skia_lib.gyp:skia_lib',
         'flags.gyp:flags',
-        'gm.gyp:gm_expectations',
-        'jsoncpp.gyp:jsoncpp',
+#        'gm.gyp:gm_expectations',
+#        'jsoncpp.gyp:jsoncpp',
         'utils.gyp:utils',
       ],
     },
