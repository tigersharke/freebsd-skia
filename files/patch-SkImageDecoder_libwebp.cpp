--- src/images/SkImageDecoder_libwebp.cpp.orig	2013-07-10 17:02:46.149120282 -0500
+++ src/images/SkImageDecoder_libwebp.cpp	2013-07-10 17:03:05.009016683 -0500
@@ -172,9 +172,9 @@
     SkBitmap::Config config = decodedBitmap->config();
 
     if (config == SkBitmap::kARGB_8888_Config) {
-        mode = premultiply ? MODE_rgbA : MODE_RGBA;
+        mode = premultiply ? MODE_RGBA : MODE_RGBA;
     } else if (config == SkBitmap::kARGB_4444_Config) {
-        mode = premultiply ? MODE_rgbA_4444 : MODE_RGBA_4444;
+        mode = premultiply ? MODE_RGBA_4444 : MODE_RGBA_4444;
     } else if (config == SkBitmap::kRGB_565_Config) {
         mode = MODE_RGB_565;
     }
