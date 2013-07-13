--- gyp/gpu.gypi.orig	2013-06-25 06:35:55.339689573 -0500
+++ gyp/gpu.gypi	2013-06-25 06:37:01.959670744 -0500
@@ -232,13 +232,13 @@
       '<(skia_include_path)/gpu/gl/SkMesaGLContext.h',
       '<(skia_src_path)/gpu/gl/mesa/SkMesaGLContext.cpp',
     ],
-    'skgpu_angle_gl_sources': [
-      '<(skia_src_path)/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',
+    #'skgpu_angle_gl_sources': [
+    #  '<(skia_src_path)/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',
 
       # Sk files
-      '<(skia_include_path)/gpu/gl/SkANGLEGLContext.h',
-      '<(skia_src_path)/gpu/gl/angle/SkANGLEGLContext.cpp',
-    ],
+    #  '<(skia_include_path)/gpu/gl/SkANGLEGLContext.h',
+    #  '<(skia_src_path)/gpu/gl/angle/SkANGLEGLContext.cpp',
+    #],
     'skgpu_debug_gl_sources': [
       '<(skia_src_path)/gpu/gl/debug/GrGLCreateDebugInterface.cpp',
       '<(skia_src_path)/gpu/gl/debug/GrFakeRefObj.h',
