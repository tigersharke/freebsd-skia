# Created by: Tigersharke
# $FreeBSD$

PORTNAME=	skia
PORTVERSION=	r10397
CATEGORIES=	devel
MASTER_SITES=	https://freebsd-skia.googlecode.com/svn-history/r63/trunk/ \
		https://github.com/tigersharke/freebsd-skia/raw/master/

MAINTAINER=	tigersharke@gmail.com
COMMENT=	2d graphics library

LICENSE=	BSD

BUILD_DEPENDS+=	gyp:${PORTSDIR}/devel/py-gyp-devel \
		${LOCALBASE}/lib/libwebp.so:${PORTSDIR}/graphics/webp \
		${LOCALBASE}/include/gif_lib.h:${PORTSDIR}/graphics/giflib \
		${LOCALBASE}/include/turbojpeg.h:${PORTSDIR}/graphics/libjpeg-turbo \
		${LOCALBASE}/include/png.h:${PORTSDIR}/graphics/png \
                ${LOCALBASE}/include/fontconfig/fontconfig.h:${PORTSDIR}/x11-fonts/fontconfig \
                ${LOCALBASE}/include/freetype2/freetype/config/ftheader.h:${PORTSDIR}/print/freetype2

WRKSRC=		${WRKDIR}

USE_GMAKE=	yes
USE_PYTHON=	yes
USE_QT4=	opengl corelib moc
USE_GL=		glu glw gl
USE_XORG=	x11
WITH_GECKO=	libxul

MAKE_ENV+=	SKIA_OUT="${WRKSRC}/built" BUILDTYPE="Release"

CXXFLAGS+=      -I${LOCALBASE}/include -DCLOCK_PROCESS_CPUTIME_ID="15" -I${LOCALBASE}/include/freetype2 \
		-I${WRKSRC}/include/config/ 
CFLAGS+=	-I${LOCALBASE}/include -I${LOCALBASE}/include/X11
LDFLAGS+=	-L${LOCALBASE}/lib

## Error was:
# /usr/local/include/ft2build.h:56:10: fatal error: 'freetype/config/ftheader.h' file not found
#                    #include <freetype/config/ftheader.h>
## Locate shows:
# /usr/local/include/freetype2/freetype/config/ftheader.h
## Answer is:
# -I${LOCALBASE}/include/freetype2 

# Unresolved error is:
# In file included from ../src/views/unix/keysym2ucs.c:37:
# ../include/views/unix/keysym2ucs.h:13:10: fatal error: 'X11/X.h' file not found
#          #include <X11/X.h>
# Locate shows:
# /usr/local/include/X11/X.h
# So I assume this ought to work, but doesn't:
# -I${LOCALBASE}/include

post-extract:
	${MKDIR} ${WRKSRC}/built

pre-build:
#	${RM}	${WRKSRC}/gyp/angle.gyp
#	${RM}	${WRKSRC}/gyp/jsoncpp.gyp
#	${RM}	${WRKSRC}/gyp/gm.gyp
	${RM}	${WRKSRC}/gyp/experimental.gyp
#	${RM} -rf	${WRKSRC}/src/gl/android
#	${RM} -rf	${WRKSRC}/src/gl/angle
#	${RM} -rf	${WRKSRC}/src/gl/iOS
#	${RM} -rf	${WRKSRC}/src/gl/win

post-build:
	${WRKSRC}/built/Debug/tests
.include <bsd.port.mk>
