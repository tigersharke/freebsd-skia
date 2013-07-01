# Created by: Tigersharke
# $FreeBSD$

PORTNAME=	skia
PORTVERSION=	r9828
CATEGORIES=	devel
MASTER_SITES=	https://github.com/tigersharke/freebsd-skia/raw/master/ \
		https://freebsd-skia.googlecode.com/svn-history/r18/trunk/

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
MAKE_ARGS+=	use_system_libwebp=1 -I${WRKSRC}/include/config/ tests
MAKE_ENV+=	use_system_libwebp=1 SKIA_OUT="${WRKSRC}/built" BUILDTYPE="Release"
USE_PYTHON=	yes
USE_QT4=	opengl corelib
USE_GL=		glu glw gl

post-extract:
	${MKDIR} ${WRKSRC}/built

pre-build:
	${CP} -R	${LOCALBASE}/include/webp ${WRKSRC}/src/images/
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
	${RM}	${WRKSRC}/gyp/angle.gyp

post-build:
	${WRKSRC}/built/Debug/tests
.include <bsd.port.mk>
