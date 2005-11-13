#
# TODO: Handle situations when there are no modules (most bconds turned off)
#
# Conditional build:
%bcond_without	alsa	# without ALSA modules
%bcond_without	arts	# without aRts module
%bcond_without	dga2	# without DGA2 module
%bcond_without	dbglib	# don't build debug versions of library
%bcond_without	esd	# without esound module
%bcond_without	fbcon	# without framebuffer module
%bcond_without	jack	# without JACK module
%bcond_without	proflib	# don't debug profiling versions of library
%bcond_without	sse	# build without sse
%bcond_without	static	# don't build static versions of library
%bcond_without	svga	# without svgalib module
%bcond_without	vga	# without vga module
#
Summary:	A game programming library
Summary(de):	Eine Bibliothek zur Programmierung von Spielen
Summary(es):	Una biblioteca de programaci�n de juegos
Summary(fr):	Une librairie de programmation de jeux
Summary(it):	Una libreria per la programmazione di videogiochi
Summary(pl):	Biblioteka do programowania gier
Name:		allegro
Version:	4.2.0
Release:	1
License:	Giftware
Group:		Libraries
Source0:	http://dl.sourceforge.net/alleg/%{name}-%{version}.tar.gz
# Source0-md5:	a8b2c85c58b16345fe735f72763f3a6e
Patch0:		%{name}-info.patch
Patch1:		%{name}-examples.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-ldflags.patch
Patch4:		%{name}-frame-pointer.patch
URL:		http://alleg.sourceforge.net/
BuildRequires:	X11-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel}
%if %{with jack}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	pkgconfig
%endif
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l de
Allegro ist eine plattform�bergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.

%description -l es
Allegro es una librer�a multi-plataforma creada para ser usada en la
programaci�n de juegos u otro tipo de programaci�n multimedia.

%description -l fr
Allegro est une librairie multi-plateforme destin�e � �tre utilis�e
dans les jeux vid�o ou d'autres types de programmation multim�dia.

%description -l it
Allegro � una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale.

%description -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%package devel
Summary:	A game programming library - header files
Summary(es):	Archivos de inclusi�n
Summary(pl):	Biblioteka do programowania gier - pliki nag��wkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains header files neccessary for compiling
applications using allegro library.

%description devel -l de
Allegro ist eine plattform�bergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket wird ben�tigt, um Programme zu bauen, die Allegro
verwenden.

%description devel -l es
Allegro es una librer�a multi-plataforma creada para ser usada en la
programaci�n de juegos u otro tipo de programaci�n multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr
Allegro est une librairie multi-plateforme destin�e � �tre utilis�e
dans les jeux vid�o ou d'autres types de programmation multim�dia. Ce
package est n�cessaire pour compiler les programmes utilisant Allegro.

%description devel -l it
Allegro � una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto � necessario per compilare programmi scritti con Allegro.

%description devel -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania
aplikacji wykorzystuj�cych bibliotek� allegro.

%package static
Summary:	A game programming library - static libraries
Summary(pl):	Biblioteka do programowania gier - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains static libraries for linking with allegro
applications.

%description static -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera biblioteki statyczne do konsolidacji z aplikacjami
wykorzystuj�cymi allegro.

%package debug
Summary:	liballd - debug version of shared allegro library
Summary(pl):	liballd - wersja debug dzielonej biblioteki allegro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description debug
liballd - debug version of shared allegro library (contains debugging
symbols and other information).

%description debug -l pl
liballd - wersja debug dzielonej biblioteki allegro (zawieraj�ca
symbole i inne informacje potrzebne przy odpluskwianiu).

%package debug-static
Summary:	liballd - debug version of static allegro library
Summary(pl):	liballd - wersja debug statycznej biblioteki allegro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description debug-static
liballd - debug version of static allegro library (contains debugging
symbols and other information).

%description debug-static -l pl
liballd - wersja debug statycznej biblioteki allegro (zawieraj�ca
symbole i inne informacje potrzebne przy odpluskwianiu).

%package profile
Summary:	liballp - profiling version of shared allegro library
Summary(pl):	liballp - wersja dzielonej biblioteki allegro s�u��ca do profilowania
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description profile
liballp - profiling version of shared allegro library.

%description profile -l pl
liballp - wersja dzielonej biblioteki allegro s�u��ca do profilowania.

%package profile-static
Summary:	liballp - profiling version of static allegro library
Summary(pl):	liballp - wersja statycznej biblioteki allegro s�u��ca do profilowania
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description profile-static
liballp - profiling version of static allegro library.

%description profile-static -l pl
liballp - wersja statycznej biblioteki allegro s�u��ca do
profilowania.

%package svgalib
Summary:	A game programming library - svgalib module
Summary(pl):	Biblioteka do programowania gier - modu� dla svgalib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description svgalib
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with allegro and svgalib.

%description svgalib -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania allegro z svgalibem.

%package dga2
Summary:	A game programming library - DGA2 module
Summary(pl):	Biblioteka do programowania gier - modu� dla DGA2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description dga2
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with DGA.

%description dga2 -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z DGA.

%package esd
Summary:	A game programming library - esound module
Summary(pl):	Biblioteka do programowania gier - modu� dla esound
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description esd
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with ESound daemon.

%description esd -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z demonem ESound.

%package arts
Summary:	A game programming library - aRts module
Summary(pl):	Biblioteka do programowania gier - modu� dla aRts
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description arts
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with aRts.

%description arts -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z aRts.

%package fbcon
Summary:	A game programming library - framebuffer module
Summary(pl):	Biblioteka do programowania gier - modu� dla framebuffera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fbcon
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with framebuffer.

%description fbcon -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z framebufferem.

%package vga
Summary:	A game programming library - vga module
Summary(pl):	Biblioteka do programowania gier - modu� dla vga
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description vga
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with vga.

%description vga -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z vga.

%package alsa
Summary:	A game programming library - ALSA modules
Summary(pl):	Biblioteka do programowania gier - modu�y dla ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	allegro-alsa9

%description alsa
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains modules for use with ALSA sound library.

%description alsa -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu�y do wykorzystania z bibliotek� d�wi�kow�
ALSA.

%package jack
Summary:	A game programming library - JACK module
Summary(pl):	Biblioteka do programowania gier - modu� dla JACK-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description jack
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with JACK sound library.

%description jack -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z bibliotek� d�wi�kow� JACK.

%package tools
Summary:	A game programming library - tools
Summary(de):	Zus�tzliche Hilfprogramme f�r die Allegro Bibliothek
Summary(es):	Herramientas adicionales para la librer�a de programaci�n Allegro
Summary(fr):	Outils suppl�mentaires pour la librairie de programmation Allegro
Summary(it):	Programmi di utilit� aggiuntivi per la libreria Allegro
Summary(pl):	Biblioteka do programowania gier - narz�dzia
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains tools.

%description tools -l de
Allegro ist eine plattform�bergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket enth�lt Programme, die f�r die Entwicklung von Allegro
Programmen hilfreich sind.

%description tools -l es
Allegro es una librer�a multi-plataforma creada para ser usada en la
programaci�n de juegos u otro tipo de programaci�n multimedia. Este
paquete contiene herramientas adicionales que son �tiles para
desarrollar programas que usen Allegro.

%description tools -l fr
Allegro est une librairie multi-plateforme destin�e � �tre utilis�e
dans les jeux vid�o ou d'autres types de programmation multim�dia. Ce
package contient des outils suppl�mentaires qui sont utiles pour le
d�veloppement de programmes avec Allegro.

%description tools -l it
Allegro � una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto contiene programmi di utilit� aggiuntivi utili allo sviluppo
di programmi con Allegro.

%description tools -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera narz�dzia.

%package tests
Summary:	A game programming library - test programs
Summary(pl):	Biblioteka do programowania gier - programy testuj�ce
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tests
This package contains programs for testing allegro library.

%description tests -l pl
Pakiet zawiera programy testuj�ce bibliotek� allegro.

%package examples
Summary:	A game programming library - examples
Summary(pl):	Biblioteka do programowania gier - programy przyk�adowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs which demonstrate allegro
features.

%description examples -l pl
Pakiet zawiera programy przyk�adowe demonstruj�ce mo�liwo�ci
biblioteki allegro.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__aclocal}
%{__autoheader} configure.in > include/allegro/platform/alunixac.hin
%{__autoconf}
TARGET_ARCH="%{rpmcflags}" export TARGET_ARCH
# dbglib & proflib are compiled besides normlib, so it's ok to have them here
%configure \
	%{?with_static:--enable-static} \
	%{?with_dbglib:--enable-dbglib} \
	%{?with_proflib:--enable-proflib} \
%if %{without alsa}
	--disable-alsadigi \
	--disable-alsamidi \
%endif
	%{!?with_arts:--disable-artsdigi} \
	%{!?with_dga2:--disable-xwin-dga2} \
	%{!?with_esd:--disable-esddigi} \
	%{!?with_fbcon:--disable-fbcon} \
	%{!?with_jack:--disable-jackdigi} \
	%{!?with_svga:--disable-svgalib} \
	%{!?with_vga:--disable-vga} \
%if %{without sse}
	--disable-sse \
	--disable-asm \
%endif
%ifnarch %{ix86}
	--disable-asm \
	--disable-mmx \
	--disable-sse
%endif

%{__make} \
	MAKEINFO=makeinfo

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man install-info install-lib \
	DESTDIR=$RPM_BUILD_ROOT

install modules.lst $RPM_BUILD_ROOT%{_libdir}/allegro/4.2

mv $RPM_BUILD_ROOT%{_bindir}/demo{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/play{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/setup{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/test{,-allegro}

# help rpm to find reqs for ELF objects
chmod 755 $RPM_BUILD_ROOT%{_libdir}/{*.so,allegro/*/*.so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES THANKS readme.txt
%attr(755,root,root) %{_libdir}/liballeg-%{version}.so
%dir %{_libdir}/allegro
%dir %{_libdir}/allegro/4.2
%{_libdir}/allegro/4.2/modules.lst

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/allegro-config
%{_libdir}/liballeg_unsharable.a
%{_includedir}/*
%{_aclocaldir}/allegro.m4
%{_mandir}/man3/*
%{_infodir}/*.info*

%if %{with static}
%files static
%defattr(644,root,root,755)
%{_libdir}/liballeg.a
%endif

%if %{with dbglib}
%files debug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballd-%{version}.so
%{_libdir}/liballd_unsharable.a

%if %{with static}
%files debug-static
%defattr(644,root,root,755)
%{_libdir}/liballd.a
%endif
%endif

%if %{with proflib}
%files profile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballp-%{version}.so
%{_libdir}/liballp_unsharable.a

%if %{with static}
%files profile-static
%defattr(644,root,root,755)
%{_libdir}/liballp.a
%endif
%endif

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-svgalib.so
%endif

%if %{with dga2}
%files dga2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-dga2.so
%endif

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-esddigi.so
%endif

%if %{with arts}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-artsdigi.so
%endif

%if %{with fbcon}
%files fbcon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-fbcon.so
%endif

%ifarch %{ix86}
%if %{with vga}
%files vga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-vga.so
%endif
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-alsadigi.so
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-alsamidi.so
%endif

%if %{with jack}
%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.2/alleg-jackdigi.so
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colormap
%attr(755,root,root) %{_bindir}/exedat
%attr(755,root,root) %{_bindir}/pack
%attr(755,root,root) %{_bindir}/rgbmap
%attr(755,root,root) %{_bindir}/textconv
%attr(755,root,root) %{_bindir}/xkeymap
%attr(755,root,root) %{_bindir}/xf2pcx
%attr(755,root,root) %{_bindir}/dat
%attr(755,root,root) %{_bindir}/dat2c
%attr(755,root,root) %{_bindir}/dat2s
%attr(755,root,root) %{_bindir}/grabber
%attr(755,root,root) %{_bindir}/pat2dat
%attr(755,root,root) %{_bindir}/setup-allegro

%files tests
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afinfo
%attr(755,root,root) %{_bindir}/akaitest
%attr(755,root,root) %{_bindir}/cpptest
%attr(755,root,root) %{_bindir}/demo-allegro
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
