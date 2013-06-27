--- gyp/views.gyp.orig	2013-06-25 06:48:03.749704603 -0500
+++ gyp/views.gyp	2013-06-25 06:49:27.079671051 -0500
@@ -22,9 +22,9 @@
         '../include/views/unix',
         '../include/xml',
       ],
-      'dependencies': [
-        'angle.gyp:*',
-      ],
+#      'dependencies': [
+#        'angle.gyp:*',
+#      ],
       'sources': [
         '../include/views/SkApplication.h',
         '../include/views/SkBGViewArtist.h',
