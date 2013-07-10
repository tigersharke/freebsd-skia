--- gyp/ports.gyp.orig	2013-07-10 06:06:26.319013253 -0500
+++ gyp/ports.gyp	2013-07-10 06:06:41.259017144 -0500
@@ -49,7 +49,7 @@
             'libraries': [
               '-lfreetype',
               '-lfontconfig',
-              '-ldl',
+              '-lc',
             ],
           },
           'sources': [
