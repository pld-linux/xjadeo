Summary:	jack video monitor
Summary(pl.UTF-8):	jack video monitor
Name:		xjadeo
Version:	0.8.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/xjadeo/%{name}-%{version}.tar.gz
# Source0-md5:	02603fb2f912763970ab778b08559978
URL:		http://xjadeo.sf.net/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	imlib2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
#BuildRequires:	libltc-devel
BuildRequires:	xorg-lib-libX11
BuildRequires:	xorg-lib-libXv-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xjadeo is a simple video player that gets sync from jack.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-portmidi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xjadeo
%attr(755,root,root) %{_bindir}/xjremote
%{_mandir}/man1/xjadeo.1*
%{_mandir}/man1/xjremote.1*
%{_datadir}/xjadeo
