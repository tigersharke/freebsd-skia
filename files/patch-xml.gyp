--- gyp/xml.gyp.orig	2013-07-25 18:13:16.955697964 -0500
+++ gyp/xml.gyp	2013-07-25 18:12:35.975694538 -0500
@@ -32,7 +32,7 @@
           '../src/xml/SkXMLPullParser.cpp', #if 0 around class decl in header
       ],
       'conditions': [
-        [ 'skia_os in ["win", "mac", "linux", "freebsd", "openbsd", "solaris", "android", "ios", "nacl", "chromeos"]', {
+        [ 'skia_os in ["win", "mac", "linux", "openbsd", "solaris", "android", "ios", "nacl", "chromeos"]', {
           'sources!': [
             # no jsapi.h by default on system
             '../include/xml/SkJS.h',
@@ -40,6 +40,15 @@
             '../src/xml/SkJSDisplayable.cpp',
           ],
         }],
+        [ 'skia_os == "freebsd"', {
+          'sources': [
+            # jsapi.h can be installed on system with libxul
+	    # /usr/local/include/libxul/jsapi.h
+            '../include/xml/SkJS.h',
+            '../src/xml/SkJS.cpp',
+            '../src/xml/SkJSDisplayable.cpp',
+          ],
+        }],
       ],
       'direct_dependent_settings': {
         'include_dirs': [
