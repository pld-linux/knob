Summary:	Simple volume control applet for KDE
Summary(pl):	Prosty aplet do kontroli g³o¶no¶ci dla KDE
Name:		knob
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://lichota.net/~krzysiek/projects/knob/%{name}-%{version}.tar.gz
# Source0-md5:	da477b2604625085441df72bdc4bb14a
Source1:        http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:  81e0b2f79ef76218381270960ac0f55f
URL:		http://lichota.net/~krzysiek/projects/knob/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knob is a simple volume control applet for KDE.

%description -l pl
Knob to prosty aplet do kontroli g³o¶no¶ci dla KDE.

%prep
%setup -q -a1

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libknob.so*
# Is it really necessary?
%{_libdir}/libknob.la
%{_datadir}/apps/kicker/applets/knob.desktop
%{_iconsdir}/hicolor/32x32/apps/knob.png
