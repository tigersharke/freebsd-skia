--- include/gpu/GrConfig.h.orig	2013-07-11 04:16:53.000000000 -0500
+++ include/gpu/GrConfig.h	2013-07-25 02:34:53.565696409 -0500
@@ -41,6 +41,9 @@
 #if !defined(GR_LINUX_BUILD)
     #define GR_LINUX_BUILD      0
 #endif
+#if !defined(GR_FREEBSD_BUILD)
+    #define GR_FREEBSD_BUILD    0
+#endif
 #if !defined(GR_MAC_BUILD)
     #define GR_MAC_BUILD        0
 #endif
@@ -57,7 +60,7 @@
 /**
  *  If no build target has been defined, attempt to infer.
  */
-#if !GR_ANDROID_BUILD && !GR_IOS_BUILD && !GR_LINUX_BUILD && !GR_MAC_BUILD && !GR_WIN32_BUILD && !GR_QNX_BUILD
+#if !GR_ANDROID_BUILD && !GR_IOS_BUILD && !GR_LINUX_BUILD !GR_FREEBSD_BUILD && !GR_MAC_BUILD && !GR_WIN32_BUILD && !GR_QNX_BUILD
     #if defined(_WIN32)
         #undef GR_WIN32_BUILD
         #define GR_WIN32_BUILD      1
@@ -82,6 +85,10 @@
         #undef GR_LINUX_BUILD
         #define GR_LINUX_BUILD      1
 //      #error "LINUX"
+    #else
+        #undef GR_FREEBSD_BUILD
+        #define GR_FREEBSD_BUILD    1
+//      #error "FREEBSD"
     #endif
 #endif
 
@@ -356,7 +363,7 @@
 /**
  *  Only one build target macro should be 1 and the rest should be 0.
  */
-#define GR_BUILD_SUM    (GR_WIN32_BUILD + GR_MAC_BUILD + GR_IOS_BUILD + GR_ANDROID_BUILD + GR_LINUX_BUILD + GR_QNX_BUILD)
+#define GR_BUILD_SUM    (GR_WIN32_BUILD + GR_MAC_BUILD + GR_IOS_BUILD + GR_ANDROID_BUILD + GR_LINUX_BUILD + GR_FREEBSD_BUILD + GR_QNX_BUILD)
 #if 0 == GR_BUILD_SUM
     #error "Missing a GR_BUILD define"
 #elif 1 != GR_BUILD_SUM
@@ -379,6 +386,9 @@
 #if GR_LINUX_BUILD
 //    #pragma message GR_WARN("GR_LINUX_BUILD")
 #endif
+#if GR_FREEBSD_BUILD
+//    #pragma message GR_WARN("GR_FREEBSD_BUILD")
+#endif
 #if GR_QNX_BUILD
 //    #pragma message GR_WARN("GR_QNX_BUILD")
 #endif
