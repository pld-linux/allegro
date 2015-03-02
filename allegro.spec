#
# Conditional build:
%bcond_without	alsa	# ALSA modules
%bcond_without	dga2	# DGA2 module
%bcond_without	jack	# JACK module
%bcond_with	svga	# svgalib module
%bcond_without	vga	# vga module (x86-only)
#
%ifnarch %{ix86}
# x86_64 too?
%undefine	with_vga
%endif
Summary:	A game programming library
Summary(de.UTF-8):	Eine Bibliothek zur Programmierung von Spielen
Summary(es.UTF-8):	Una biblioteca de programación de juegos
Summary(fr.UTF-8):	Une librairie de programmation de jeux
Summary(it.UTF-8):	Una libreria per la programmazione di videogiochi
Summary(pl.UTF-8):	Biblioteka do programowania gier
Name:		allegro
Version:	4.4.2
Release:	6
License:	Giftware
Group:		Libraries
Source0:	http://downloads.sourceforge.net/alleg/%{name}-%{version}.tar.gz
# Source0-md5:	4db71b0460fc99926ae91d223199c2e6
Patch0:		%{name}-info.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-man-prefix.patch
Patch3:		%{name}-format.patch
URL:		http://alleg.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
BuildRequires:	cmake >= 2.6
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l de.UTF-8
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.

%description -l es.UTF-8
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia.

%description -l fr.UTF-8
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia.

%description -l it.UTF-8
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale.

%description -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%package devel
Summary:	A game programming library - header files
Summary(es.UTF-8):	Archivos de inclusión
Summary(pl.UTF-8):	Biblioteka do programowania gier - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXxf86vm-devel
Obsoletes:	allegro-static

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains header files neccessary for compiling
applications using allegro library.

%description devel -l de.UTF-8
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket wird benötigt, um Programme zu bauen, die Allegro
verwenden.

%description devel -l es.UTF-8
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr.UTF-8
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package est nécessaire pour compiler les programmes utilisant Allegro.

%description devel -l it.UTF-8
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto è necessario per compilare programmi scritti con Allegro.

%description devel -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilowania
aplikacji wykorzystujących bibliotekę allegro.

%package dga2
Summary:	A game programming library - DGA2 module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla DGA2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description dga2
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with DGA.

%description dga2 -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z DGA.

%package fbcon
Summary:	A game programming library - FrameBuffer module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla FrameBuffera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fbcon
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with Linux FrameBuffer.

%description fbcon -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z linuksowym FrameBufferem.

%package svgalib
Summary:	A game programming library - svgalib module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla svgalib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description svgalib
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with allegro and svgalib.

%description svgalib -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania allegro z svgalibem.

%package vga
Summary:	A game programming library - vga module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla vga
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description vga
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with vga.

%description vga -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z vga.

%package alsa
Summary:	A game programming library - ALSA modules
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduły dla ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	allegro-alsa9

%description alsa
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains modules for use with ALSA sound library.

%description alsa -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduły do wykorzystania z biblioteką dźwiękową
ALSA.

%package jack
Summary:	A game programming library - JACK module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla JACK-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description jack
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with JACK sound library.

%description jack -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z biblioteką dźwiękową JACK.

%package addons
Summary:	Allegro addon libraries
Summary(pl.UTF-8):	Dodatkowe biblioteki Allegro
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	allegro-gl

%description addons
Allegro addon libraries: AllegroGL, JPGAlleg, loadpng, logg.

%description addons -l pl.UTF-8
Dodatkowe biblioteki Allegro: AllegroGL, JPGAlleg, loadpng, logg.

%package addons-devel
Summary:	Header files for Allegro addon libraries
Summary(pl.UTF-8):	Pliki nagłówkowe dodatkowych bibliotek Allegro
Group:		Development/Libraries
Requires:	%{name}-addons = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	OpenGL-devel
Requires:	libpng-devel
Requires:	libvorbis-devel
Obsoletes:	allegro-gl-devel

%description addons-devel
Header files for Allegro addon libraries: AllegroGL, JPGAlleg,
loadpng, logg.

%description addons-devel -l pl.UTF-8
Pliki nagłówkowe dodatkowych bibliotek Allegro: AllegroGL, JPGAlleg,
loadpng, logg.

%package tools
Summary:	A game programming library - tools
Summary(de.UTF-8):	Zusätzliche Hilfprogramme für die Allegro Bibliothek
Summary(es.UTF-8):	Herramientas adicionales para la librería de programación Allegro
Summary(fr.UTF-8):	Outils supplémentaires pour la librairie de programmation Allegro
Summary(it.UTF-8):	Programmi di utilità aggiuntivi per la libreria Allegro
Summary(pl.UTF-8):	Biblioteka do programowania gier - narzędzia
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains tools.

%description tools -l de.UTF-8
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket enthält Programme, die für die Entwicklung von Allegro
Programmen hilfreich sind.

%description tools -l es.UTF-8
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete contiene herramientas adicionales que son útiles para
desarrollar programas que usen Allegro.

%description tools -l fr.UTF-8
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package contient des outils supplémentaires qui sont utiles pour le
développement de programmes avec Allegro.

%description tools -l it.UTF-8
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto contiene programmi di utilità aggiuntivi utili allo sviluppo
di programmi con Allegro.

%description tools -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera narzędzia.

%package tests
Summary:	A game programming library - test programs
Summary(pl.UTF-8):	Biblioteka do programowania gier - programy testujące
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tests
This package contains programs for testing allegro library.

%description tests -l pl.UTF-8
Pakiet zawiera programy testujące bibliotekę allegro.

%package examples
Summary:	A game programming library - examples
Summary(pl.UTF-8):	Biblioteka do programowania gier - programy przykładowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs which demonstrate allegro
features.

%description examples -l pl.UTF-8
Pakiet zawiera programy przykładowe demonstrujące możliwości
biblioteki allegro.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__sed} -i -e 's/ADDON_LINKAGE STATIC/ADDON_LINKAGE SHARED/' CMakeLists.txt

%build
install -d build
cd build
%cmake .. \
	-DINFODIR=%{_infodir} \
	-DPLATFORM_LIBS=-ldl \
	%{!?with_alsa:-DWANT_ALSA=OFF} \
	-DWANT_LINUX_CONSOLE=ON \
	%{!?with_vga:-DWANT_LINUX_VGA=OFF} \
	%{!?with_svga:-DWANT_LINUX_SVGALIB=OFF}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install modules.lst $RPM_BUILD_ROOT%{_libdir}/allegro/%{version}

# install examples and tests
find build/examples -maxdepth 1 -perm 755 -name "ex*" -exec install {} $RPM_BUILD_ROOT%{_bindir} \;
find build/tests -maxdepth 1 -perm 755 ! -name CMakeFiles -exec install {} $RPM_BUILD_ROOT%{_bindir} \;

# force install man pages
cp build/docs/man/* $RPM_BUILD_ROOT%{_mandir}/man3

mv $RPM_BUILD_ROOT%{_bindir}/play{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/test{,-allegro}

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/allegro-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	addons -p /sbin/ldconfig
%postun	addons -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES THANKS readme.txt todo.txt
%attr(755,root,root) %{_libdir}/liballeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballeg.so.4.4
%dir %{_libdir}/allegro
%dir %{_libdir}/allegro/%{version}
%{_libdir}/allegro/%{version}/modules.lst

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/allegro-config
%attr(755,root,root) %{_libdir}/liballeg.so
%{_includedir}/allegro
%{_includedir}/allegro.h
%{_includedir}/linalleg.h
%{_includedir}/xalleg.h
# original names were too generic, man-prefix patch adds "allegro-" prefix
%{_mandir}/man3/allegro-*.3*
%{_infodir}/allegro.info*
%{_pkgconfigdir}/allegro.pc

%if %{with dga2}
%files dga2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-dga2.so
%endif

%files fbcon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-fbcon.so

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-svgalib.so
%endif

%if %{with vga}
%files vga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-vga.so
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-alsadigi.so
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-alsamidi.so
%endif

%if %{with jack}
%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-jack.so
%endif

%files addons
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballeggl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballeggl.so.4.4
%attr(755,root,root) %{_libdir}/libjpgalleg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpgalleg.so.4.4
%attr(755,root,root) %{_libdir}/libloadpng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libloadpng.so.4.4
%attr(755,root,root) %{_libdir}/liblogg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblogg.so.4.4

%files addons-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballeggl.so
%attr(755,root,root) %{_libdir}/libjpgalleg.so
%attr(755,root,root) %{_libdir}/libloadpng.so
%attr(755,root,root) %{_libdir}/liblogg.so
%{_includedir}/allegrogl
%{_includedir}/alleggl.h
%{_includedir}/jpgalleg.h
%{_includedir}/loadpng.h
%{_includedir}/logg.h
%{_pkgconfigdir}/allegrogl.pc
%{_pkgconfigdir}/jpgalleg.pc
%{_pkgconfigdir}/loadpng.pc
%{_pkgconfigdir}/logg.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colormap
%attr(755,root,root) %{_bindir}/exedat
%attr(755,root,root) %{_bindir}/pack
%attr(755,root,root) %{_bindir}/rgbmap
%attr(755,root,root) %{_bindir}/textconv
%attr(755,root,root) %{_bindir}/dat
%attr(755,root,root) %{_bindir}/dat2c
%attr(755,root,root) %{_bindir}/dat2s
%attr(755,root,root) %{_bindir}/grabber
%attr(755,root,root) %{_bindir}/pat2dat

%files tests
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afinfo
%attr(755,root,root) %{_bindir}/akaitest
%attr(755,root,root) %{_bindir}/digitest
%attr(755,root,root) %{_bindir}/filetest
%attr(755,root,root) %{_bindir}/gfxinfo
%attr(755,root,root) %{_bindir}/mathtest
%attr(755,root,root) %{_bindir}/miditest
%attr(755,root,root) %{_bindir}/play-allegro
%attr(755,root,root) %{_bindir}/playfli
%attr(755,root,root) %{_bindir}/test-allegro
%attr(755,root,root) %{_bindir}/vesainfo

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex12bit
%attr(755,root,root) %{_bindir}/ex3buf
%attr(755,root,root) %{_bindir}/ex3d
%attr(755,root,root) %{_bindir}/exaccel
%attr(755,root,root) %{_bindir}/exalpha
%attr(755,root,root) %{_bindir}/exbitmap
%attr(755,root,root) %{_bindir}/exblend
%attr(755,root,root) %{_bindir}/excamera
%attr(755,root,root) %{_bindir}/excolmap
%attr(755,root,root) %{_bindir}/exconfig
%attr(755,root,root) %{_bindir}/excustom
%attr(755,root,root) %{_bindir}/exdata
%attr(755,root,root) %{_bindir}/exdbuf
%attr(755,root,root) %{_bindir}/exexedat
%attr(755,root,root) %{_bindir}/exfixed
%attr(755,root,root) %{_bindir}/exflame
%attr(755,root,root) %{_bindir}/exflip
%attr(755,root,root) %{_bindir}/exfont
%attr(755,root,root) %{_bindir}/exgui
%attr(755,root,root) %{_bindir}/exhello
%attr(755,root,root) %{_bindir}/exjoy
%attr(755,root,root) %{_bindir}/exkeys
%attr(755,root,root) %{_bindir}/exlights
%attr(755,root,root) %{_bindir}/exmem
%attr(755,root,root) %{_bindir}/exmidi
%attr(755,root,root) %{_bindir}/exmouse
%attr(755,root,root) %{_bindir}/expackf
%attr(755,root,root) %{_bindir}/expal
%attr(755,root,root) %{_bindir}/expat
%attr(755,root,root) %{_bindir}/exquat
%attr(755,root,root) %{_bindir}/exrgbhsv
%attr(755,root,root) %{_bindir}/exrotscl
%attr(755,root,root) %{_bindir}/extrans2
%attr(755,root,root) %{_bindir}/exsample
%attr(755,root,root) %{_bindir}/exsyscur
%attr(755,root,root) %{_bindir}/exscale
%attr(755,root,root) %{_bindir}/exscn3d
%attr(755,root,root) %{_bindir}/exscroll
%attr(755,root,root) %{_bindir}/exshade
%attr(755,root,root) %{_bindir}/exspline
%attr(755,root,root) %{_bindir}/exsprite
%attr(755,root,root) %{_bindir}/exstars
%attr(755,root,root) %{_bindir}/exstream
%attr(755,root,root) %{_bindir}/exswitch
%attr(755,root,root) %{_bindir}/extimer
%attr(755,root,root) %{_bindir}/extrans
%attr(755,root,root) %{_bindir}/extruec
%attr(755,root,root) %{_bindir}/exunicod
%attr(755,root,root) %{_bindir}/exupdate
%attr(755,root,root) %{_bindir}/exxfade
%attr(755,root,root) %{_bindir}/exzbuf
