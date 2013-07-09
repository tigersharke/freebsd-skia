--- gyp/libwebp.gyp.orig	2013-07-08 23:38:06.815982242 -0500
+++ gyp/libwebp.gyp	2013-07-08 23:37:19.436446737 -0500
@@ -4,7 +4,7 @@
 
 {
   'variables': {
-    'use_system_libwebp%': 0,
+    'use_system_libwebp%': 1,
   },
   'conditions': [
     ['use_system_libwebp==0', {
