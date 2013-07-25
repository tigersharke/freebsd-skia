--- gyp/debugger.gyp.orig	2013-07-11 04:16:54.000000000 -0500
+++ gyp/debugger.gyp	2013-07-25 03:23:24.675695478 -0500
@@ -1,7 +1,7 @@
 {
   'variables': {
     'conditions': [
-      [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris", "chromeos"]', {
+      [ 'skia_os in ["linux", "openbsd", "solaris", "chromeos"]', {
         # Use the systemwide Qt libs by default
         'variables': {
           'qt_sdk%': '/usr',
@@ -27,6 +27,25 @@
           '-lQtOpenGL'
         ],
       }],
+      [ 'skia_os == "freebsd"', {
+        'variables': {
+          'qt_sdk%': '/usr/local',
+        },
+        'qt_sdk': '<(qt_sdk)',
+        'qt_moc%': 'moc-qt4',
+        'qt_includes': [
+          '<(qt_sdk)/include/qt4',
+          '<(qt_sdk)/include/qt4/Qt',
+          '<(qt_sdk)/include/qt4/QtCore',
+          '<(qt_sdk)/include/qt4/QtGui',
+          '<(qt_sdk)/include/qt4/QtOpenGL',
+        ],
+        'qt_libs': [
+          '-lQtCore',
+          '-lQtGui',
+          '-lQtOpenGL'
+        ],
+      }],
       [ 'skia_os == "mac"', {
         # Use the systemwide Qt libs by default
         'variables': {
