# Created by: Tigersharke
# $FreeBSD$

PORTNAME=	skia
PORTVERSION=	r9949
CATEGORIES=	devel
MASTER_SITES=	https://github.com/tigersharke/freebsd-skia/raw/master/ \
		https://freebsd-skia.googlecode.com/svn-history/r27/trunk/

MAINTAINER=	tigersharke@gmail.com
COMMENT=	2d graphics library

LICENSE=	BSD

BUILD_DEPENDS+=	${LOCALBASE}/bin/gyp:${PORTSDIR}/devel/py-gyp-devel \
		${LOCALBASE}/lib/libwebp.so:${PORTSDIR}/graphics/webp \
		${LOCALBASE}/include/gif_lib.h:${PORTSDIR}/graphics/giflib \
		${LOCALBASE}/include/jpeglib.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jconfig.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jmorecfg.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/jerror.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/turbojpeg.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/png.h:${PORTSDIR}/graphics/png \
		${LOCALBASE}/include/pnglibconf.h:${PORTSDIR}/graphics/png \
		${LOCALBASE}/include/pngconf.h:${PORTSDIR}/graphics/png \
                ${LOCALBASE}/include/fontconfig/fontconfig.h:${PORTSDIR}/x11-fonts/fontconfig \
                ${LOCALBASE}/include/freetype2/freetype/config/ftheader.h:${PORTSDIR}/print/freetype2

WRKSRC=		${WRKDIR}

USE_GMAKE=	yes
#MAKE_ARGS+=	tests
MAKE_ARGS+=	-I${WRKSRC}/include/config/
MAKE_ENV+=	SKIA_OUT="${WRKSRC}/built" BUILDTYPE="Release"
USE_PYTHON=	yes
USE_QT4=	opengl corelib
USE_GL=		glu glw gl

CXXFLAGS+=      -Iinclude -I${LOCALBASE}/lib -I${LOCALBASE}/include -I${LOCALBASE}/lib/webp \
                -I${LOCALBASE}/include/fontconfig -I${LOCALBASE}/include/freetype2/freetype/config \
                -I${LOCALBASE}/include/freetype2 -I${LOCALBASE}/lib/libgif.so -DCLOCK_PROCESS_CPUTIME_ID="15"

post-extract:
	${MKDIR} ${WRKSRC}/built

pre-build:
#	${CP} -R	${LOCALBASE}/include/webp ${WRKSRC}/src/images/
##	${CP}	${LOCALBASE}/include/gif_lib.h ${WRKSRC}/src/images
#	${CP}	${LOCALBASE}/include/jconfig.h ${WRKSRC}/src/tools
#	${CP}	${LOCALBASE}/include/jerror.h ${WRKSRC}/src/tools
#	${CP}	${LOCALBASE}/include/jmorecfg.h ${WRKSRC}/src/tools
#	${CP}	${LOCALBASE}/include/jpeglib.h ${WRKSRC}/src/tools
#	${CP}	${LOCALBASE}/include/turbojpeg.h ${WRKSRC}/src/tools
##	${CP}	${LOCALBASE}/include/jpegint.h ${WRKSRC}/src/images
#	${CP}	${LOCALBASE}/include/jerror.h ${WRKSRC}/src/tools
##	${CP}	${LOCALBASE}/include/png.h ${WRKSRC}/src/images
##	${CP}	${LOCALBASE}/include/pnglibconf.h ${WRKSRC}/src/images
##	${CP}	${LOCALBASE}/include/pngconf.h ${WRKSRC}/src/images
##
	${RM}	${WRKSRC}/gyp/angle.gyp

post-build:
	${WRKSRC}/built/Debug/tests
.include <bsd.port.mk>
