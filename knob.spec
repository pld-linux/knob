Summary:	Simple volume control applet for KDE
Summary(pl):	Prosty aplet do kontroli g�o�no�ci dla KDE
Name:		knob
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://lichota.net/~krzysiek/projects/knob/%{name}-%{version}.tar.gz
URL:		http://lichota.net/~krzysiek/projects/knob/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Knob is a simple volume control applet for KDE.

%description -l pl
Knob to prosty aplet do kontroli g�o�no�ci dla KDE.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libknob.*
%{_datadir}/apps/*
%{_datadir}/pixmaps/locolor/32x32/apps/knob.png