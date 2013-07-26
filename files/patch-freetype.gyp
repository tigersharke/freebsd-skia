--- gyp/freetype.gyp.orig	2013-07-24 21:29:26.000000000 -0500
+++ gyp/freetype.gyp	2013-07-25 18:22:27.735695119 -0500
@@ -4,7 +4,7 @@
       'target_name': 'freetype',
       'type': 'none',
       'conditions': [
-        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris", "chromeos"]', {
+        [ 'skia_os in ["linux", "openbsd", "solaris", "chromeos"]', {
           'direct_dependent_settings': {
             'include_dirs' : [
               '/usr/include/freetype2',
@@ -21,6 +21,23 @@
             }
           },
         }],
+        [ 'skia_os == "freebsd"', {
+          'direct_dependent_settings': {
+            'include_dirs' : [
+              '/usr/local/include/freetype2',
+            ],
+            'link_settings': {
+              'libraries': [
+                '-lfreetype',
+              ],
+              'defines': [
+                #The font host requires at least FreeType 2.3.0 at runtime.
+                'SK_FONTHOST_FREETYPE_RUNTIME_VERSION=0x020300',\
+                'SK_CAN_USE_DLOPEN=1',
+              ],
+            }
+          },
+        }],
         [ 'skia_os in ["android", "nacl"]', {
           'dependencies': [
             'freetype_static'
