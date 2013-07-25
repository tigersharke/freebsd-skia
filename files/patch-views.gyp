--- gyp/views.gyp.orig	2013-07-24 23:38:39.608331970 -0500
+++ gyp/views.gyp	2013-07-24 23:39:55.176372495 -0500
@@ -13,7 +13,7 @@
       'standalone_static_library': 1,
       'dependencies': [
         'skia_lib.gyp:skia_lib',
-        'angle.gyp:*',
+#        'angle.gyp:*',
         'xml.gyp:*',
       ],
       'include_dirs': [
