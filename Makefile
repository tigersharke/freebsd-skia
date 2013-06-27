# Created by: Tigersharke
# $FreeBSD$

PORTNAME=	skia
PORTVERSION=	r9785
CATEGORIES=	devel
#MASTER_SITES=	http://

MAINTAINER=	tigersharke@gmail.com
COMMENT=	2d graphics library

LICENSE=	BSD

BUILD_DEPENDS+=	${LOCALBASE}/bin/gyp:${PORTSDIR}/devel/py-gyp-devel \
		${LOCALBASE}/lib/libwebp.so:${PORTSDIR}/graphics/webp \
		${LOCALBASE}/include/gif_lib.h:${PORTSDIR}/graphics/giflib \
		${LOCALBASE}/include/jpeglib.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jconfig.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jmorecfg.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jpegint.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jerror.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/png.h:${PORTSDIR}/graphics/png \
		${LOCALBASE}/include/pnglibconf.h:${PORTSDIR}/graphics/png \
		${LOCALBASE}/include/pngconf.h:${PORTSDIR}/graphics/png

WRKSRC=		${WRKDIR}

USE_GMAKE=	yes
MAKE_ARGS+=	use_system_libwebp=1 tests
MAKE_ENV+=	use_system_libwebp=1 SKIA_OUT="${WRKSRC}/built" BUILDTYPE="Release"
USE_PYTHON=	yes
USE_QT4=	opengl corelib
USE_GL=		glu glw gl

post-extract:
	${MKDIR} ${WRKSRC}/built

pre-build:
	${CP}	${LOCALBASE}/lib/libwebp.a ${WRKSRC}/third_party/externals
	${CP}	${LOCALBASE}/lib/libwebp.la ${WRKSRC}/src/effects
	${CP}	${LOCALBASE}/lib/libwebp.so ${WRKSRC}/src/effects
	${CP}	${LOCALBASE}/lib/libwebp.so.2 ${WRKSRC}/src/effects
	${CP}	${LOCALBASE}/include/gif_lib.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/jpeglib.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/jconfig.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/jmorecfg.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/jpegint.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/jerror.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/png.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/pnglibconf.h ${WRKSRC}/src/images
	${CP}	${LOCALBASE}/include/pngconf.h ${WRKSRC}/src/images
#
	${MV}	${WRKSRC}/gyp/angle.gyp ${WRKSRC}/gyp/ignore-angle.gyp
#	${MV}	${WRKSRC}/gyp/libwebp.gyp ${WRKSRC}/gyp/ignore-libwebp.gyp

post-build:
	${WRKSRC}/built/Debug/tests
.include <bsd.port.mk>
