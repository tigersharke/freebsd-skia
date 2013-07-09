--- gyp/utils.gyp.orig	2013-07-05 01:20:55.773268804 -0500
+++ gyp/utils.gyp	2013-07-05 01:25:08.256018920 -0500
@@ -91,7 +91,7 @@
         '../src/utils/SkThreadUtils.h',
         '../src/utils/SkThreadUtils_pthread.cpp',
         '../src/utils/SkThreadUtils_pthread.h',
-        '../src/utils/SkThreadUtils_pthread_linux.cpp',
+#        '../src/utils/SkThreadUtils_pthread_linux.cpp',
         '../src/utils/SkThreadUtils_pthread_mach.cpp',
         '../src/utils/SkThreadUtils_pthread_other.cpp',
         '../src/utils/SkThreadUtils_win.cpp',
