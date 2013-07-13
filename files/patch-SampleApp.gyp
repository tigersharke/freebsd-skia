--- gyp/SampleApp.gyp.orig	2013-07-13 06:14:26.412106221 -0500
+++ gyp/SampleApp.gyp	2013-07-13 06:15:15.068973520 -0500
@@ -151,7 +151,7 @@
         'views.gyp:views',
         'animator.gyp:animator',
         'xml.gyp:xml',
-        'experimental.gyp:experimental',
+#        'experimental.gyp:experimental',
         'pdf.gyp:pdf',
         'views_animated.gyp:views_animated',
         'lua.gyp:lua',
@@ -165,7 +165,7 @@
            'pdfviewer.gyp:libpdfviewer',
          ],
          'include_dirs' : [
-           '../experimental/PdfViewer/',
+#           '../experimental/PdfViewer/',
          ],
          'sources': [
            '../samplecode/SamplePdfFileViewer.cpp',
