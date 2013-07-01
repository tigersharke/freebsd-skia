--- gyp/libwebp.gyp.orig	2013-06-24 03:19:50.000000000 -0500
+++ gyp/libwebp.gyp	2013-06-25 07:39:45.209704617 -0500
@@ -9,110 +9,110 @@
   'conditions': [
     ['use_system_libwebp==0', {
       'targets': [
-        {
-          'target_name': 'libwebp_dec',
-          'type': 'static_library',
-          'include_dirs': [
-              '../third_party/externals/libwebp',
-          ],
-          'sources': [
-            '../third_party/externals/libwebp/src/dec/alpha.c',
-            '../third_party/externals/libwebp/src/dec/buffer.c',
-            '../third_party/externals/libwebp/src/dec/frame.c',
-            '../third_party/externals/libwebp/src/dec/idec.c',
-            '../third_party/externals/libwebp/src/dec/io.c',
-            '../third_party/externals/libwebp/src/dec/layer.c',
-            '../third_party/externals/libwebp/src/dec/quant.c',
-            '../third_party/externals/libwebp/src/dec/tree.c',
-            '../third_party/externals/libwebp/src/dec/vp8.c',
-            '../third_party/externals/libwebp/src/dec/vp8l.c',
-            '../third_party/externals/libwebp/src/dec/webp.c',
-          ],
-        },
-        {
-          'target_name': 'libwebp_demux',
-          'type': 'static_library',
-          'include_dirs': [
-              '../third_party/externals/libwebp',
-          ],
-          'sources': [
-            '../third_party/externals/libwebp/src/demux/demux.c',
-          ],
-        },
-        {
-          'target_name': 'libwebp_dsp',
-          'type': 'static_library',
-          'include_dirs': [
-              '../third_party/externals/libwebp',
-          ],
-          'sources': [
-            '../third_party/externals/libwebp/src/dsp/cpu.c',
-            '../third_party/externals/libwebp/src/dsp/dec.c',
-            '../third_party/externals/libwebp/src/dsp/dec_sse2.c',
-            '../third_party/externals/libwebp/src/dsp/enc.c',
-            '../third_party/externals/libwebp/src/dsp/enc_sse2.c',
-            '../third_party/externals/libwebp/src/dsp/lossless.c',
-            '../third_party/externals/libwebp/src/dsp/upsampling.c',
-            '../third_party/externals/libwebp/src/dsp/upsampling_sse2.c',
-            '../third_party/externals/libwebp/src/dsp/yuv.c',
-          ],
-          'conditions': [
-            ['skia_os == "android"', {
-              'dependencies' : [
-                'android_deps.gyp:cpu_features',
-              ],
-            }],
-          ],
-        },
-        {
-          'target_name': 'libwebp_dsp_neon',
-          'conditions': [
-            ['armv7 == 1', {
-              'type': 'static_library',
-              'include_dirs': [
-                  '../third_party/externals/libwebp',
-              ],
-              'sources': [
-                '../third_party/externals/libwebp/src/dsp/dec_neon.c',
-                '../third_party/externals/libwebp/src/dsp/enc_neon.c',
-                '../third_party/externals/libwebp/src/dsp/upsampling_neon.c',
-              ],
-              # behavior similar dsp_neon.c.neon in an Android.mk
-              'cflags!': [
-                '-mfpu=vfpv3-d16',
-              ],
-              'cflags': [ '-mfpu=neon' ],
-            },{  # "armv7 != 1"
-              'type': 'none',
-            }],
-          ],
-        },
-        {
-          'target_name': 'libwebp_enc',
-          'type': 'static_library',
-          'include_dirs': [
-              '../third_party/externals/libwebp',
-          ],
-          'sources': [
-            '../third_party/externals/libwebp/src/enc/alpha.c',
-            '../third_party/externals/libwebp/src/enc/analysis.c',
-            '../third_party/externals/libwebp/src/enc/backward_references.c',
-            '../third_party/externals/libwebp/src/enc/config.c',
-            '../third_party/externals/libwebp/src/enc/cost.c',
-            '../third_party/externals/libwebp/src/enc/filter.c',
-            '../third_party/externals/libwebp/src/enc/frame.c',
-            '../third_party/externals/libwebp/src/enc/histogram.c',
-            '../third_party/externals/libwebp/src/enc/iterator.c',
-            '../third_party/externals/libwebp/src/enc/layer.c',
-            '../third_party/externals/libwebp/src/enc/picture.c',
-            '../third_party/externals/libwebp/src/enc/quant.c',
-            '../third_party/externals/libwebp/src/enc/syntax.c',
-            '../third_party/externals/libwebp/src/enc/token.c',
-            '../third_party/externals/libwebp/src/enc/tree.c',
-            '../third_party/externals/libwebp/src/enc/vp8l.c',
-            '../third_party/externals/libwebp/src/enc/webpenc.c',
-          ],
-        },
+#        {
+#          'target_name': 'libwebp_dec',
+#          'type': 'static_library',
+#          'include_dirs': [
+#              '../third_party/externals/libwebp',
+#          ],
+#          'sources': [
+#            '../third_party/externals/libwebp/src/dec/alpha.c',
+#            '../third_party/externals/libwebp/src/dec/buffer.c',
+#            '../third_party/externals/libwebp/src/dec/frame.c',
+#            '../third_party/externals/libwebp/src/dec/idec.c',
+#            '../third_party/externals/libwebp/src/dec/io.c',
+#            '../third_party/externals/libwebp/src/dec/layer.c',
+#            '../third_party/externals/libwebp/src/dec/quant.c',
+#            '../third_party/externals/libwebp/src/dec/tree.c',
+#            '../third_party/externals/libwebp/src/dec/vp8.c',
+#            '../third_party/externals/libwebp/src/dec/vp8l.c',
+#            '../third_party/externals/libwebp/src/dec/webp.c',
+#          ],
+#        },
+#        {
+#          'target_name': 'libwebp_demux',
+#          'type': 'static_library',
+#          'include_dirs': [
+#              '../third_party/externals/libwebp',
+#          ],
+#          'sources': [
+#            '../third_party/externals/libwebp/src/demux/demux.c',
+#          ],
+#        },
+#        {
+#          'target_name': 'libwebp_dsp',
+#          'type': 'static_library',
+#          'include_dirs': [
+#              '../third_party/externals/libwebp',
+#          ],
+#          'sources': [
+#            '../third_party/externals/libwebp/src/dsp/cpu.c',
+#            '../third_party/externals/libwebp/src/dsp/dec.c',
+#            '../third_party/externals/libwebp/src/dsp/dec_sse2.c',
+#            '../third_party/externals/libwebp/src/dsp/enc.c',
+#            '../third_party/externals/libwebp/src/dsp/enc_sse2.c',
+#            '../third_party/externals/libwebp/src/dsp/lossless.c',
+#            '../third_party/externals/libwebp/src/dsp/upsampling.c',
+#            '../third_party/externals/libwebp/src/dsp/upsampling_sse2.c',
+#            '../third_party/externals/libwebp/src/dsp/yuv.c',
+#          ],
+#          'conditions': [
+#            ['skia_os == "android"', {
+#              'dependencies' : [
+#                'android_deps.gyp:cpu_features',
+#              ],
+#            }],
+#          ],
+#        },
+#        {
+#          'target_name': 'libwebp_dsp_neon',
+#          'conditions': [
+#            ['armv7 == 1', {
+#              'type': 'static_library',
+#              'include_dirs': [
+#                  '../third_party/externals/libwebp',
+#              ],
+#              'sources': [
+#                '../third_party/externals/libwebp/src/dsp/dec_neon.c',
+#                '../third_party/externals/libwebp/src/dsp/enc_neon.c',
+#                '../third_party/externals/libwebp/src/dsp/upsampling_neon.c',
+#              ],
+#              # behavior similar dsp_neon.c.neon in an Android.mk
+#              'cflags!': [
+#                '-mfpu=vfpv3-d16',
+#              ],
+#              'cflags': [ '-mfpu=neon' ],
+#            },{  # "armv7 != 1"
+#              'type': 'none',
+#            }],
+#          ],
+#        },
+#        {
+#          'target_name': 'libwebp_enc',
+#          'type': 'static_library',
+#          'include_dirs': [
+#              '../third_party/externals/libwebp',
+#          ],
+#          'sources': [
+#            '../third_party/externals/libwebp/src/enc/alpha.c',
+#            '../third_party/externals/libwebp/src/enc/analysis.c',
+#            '../third_party/externals/libwebp/src/enc/backward_references.c',
+#            '../third_party/externals/libwebp/src/enc/config.c',
+#            '../third_party/externals/libwebp/src/enc/cost.c',
+#            '../third_party/externals/libwebp/src/enc/filter.c',
+#            '../third_party/externals/libwebp/src/enc/frame.c',
+#            '../third_party/externals/libwebp/src/enc/histogram.c',
+#            '../third_party/externals/libwebp/src/enc/iterator.c',
+#            '../third_party/externals/libwebp/src/enc/layer.c',
+#            '../third_party/externals/libwebp/src/enc/picture.c',
+#            '../third_party/externals/libwebp/src/enc/quant.c',
+#            '../third_party/externals/libwebp/src/enc/syntax.c',
+#            '../third_party/externals/libwebp/src/enc/token.c',
+#            '../third_party/externals/libwebp/src/enc/tree.c',
+#            '../third_party/externals/libwebp/src/enc/vp8l.c',
+#            '../third_party/externals/libwebp/src/enc/webpenc.c',
+#          ],
+#        },
         {
           'target_name': 'libwebp_utils',
           'type': 'static_library',
@@ -127,7 +127,7 @@
             '../third_party/externals/libwebp/src/utils/huffman.c',
             '../third_party/externals/libwebp/src/utils/huffman_encode.c',
             '../third_party/externals/libwebp/src/utils/quant_levels.c',
-            '../third_party/externals/libwebp/src/utils/quant_levels_dec.c',
+#            '../third_party/externals/libwebp/src/utils/quant_levels_dec.c',
             '../third_party/externals/libwebp/src/utils/rescaler.c',
             '../third_party/externals/libwebp/src/utils/thread.c',
             '../third_party/externals/libwebp/src/utils/utils.c',
@@ -137,11 +137,11 @@
           'target_name': 'libwebp',
           'type': 'none',
           'dependencies' : [
-            'libwebp_dec',
-            'libwebp_demux',
-            'libwebp_dsp',
-            'libwebp_dsp_neon',
-            'libwebp_enc',
+#            'libwebp_dec',
+#            'libwebp_demux',
+#            'libwebp_dsp',
+#            'libwebp_dsp_neon',
+#            'libwebp_enc',
             'libwebp_utils',
           ],
           'direct_dependent_settings': {
