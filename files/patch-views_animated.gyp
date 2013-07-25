--- gyp/views_animated.gyp.orig	2013-07-24 23:42:24.585703771 -0500
+++ gyp/views_animated.gyp	2013-07-24 23:42:41.096512519 -0500
@@ -7,7 +7,7 @@
       'type': 'static_library',
       'dependencies': [
         'skia_lib.gyp:skia_lib',
-        'angle.gyp:*',
+#        'angle.gyp:*',
         'animator.gyp:*',
         'views.gyp:*',
         'xml.gyp:*',
