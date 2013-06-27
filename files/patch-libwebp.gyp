--- gyp/libwebp.gyp.orig	2013-06-27 01:08:28.999689650 -0500
+++ gyp/libwebp.gyp	2013-06-27 01:09:06.839690544 -0500
@@ -4,7 +4,7 @@
 
 {
   'variables': {
-    'use_system_libwebp%': 0,
+    'use_system_libwebp%': 1,
   },
   'conditions': [
     ['use_system_libwebp==0', {
