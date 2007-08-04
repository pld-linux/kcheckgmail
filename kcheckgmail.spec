Summary:	KDE systray application to check your Gmail
Summary(pl.UTF-8):	Aplikacja do sprawdzania Gmaila w zasobniku KDE
Name:		kcheckgmail
Version:	0.5.7
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kcheckgmail/%{name}-%{version}.tar.bz2
# Source0-md5:	c0643c1b9c0453a9144199c6f0d20390
Source1:	%{name}.desktop
Source2:	%{name}-pl.po
Patch0:		%{name}-firefox-name.patch
URL:		http://kcheckgmail.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.6.1
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE systray application to check your Gmail.

%description -l pl.UTF-8
Aplikacja do sprawdzania Gmaila w zasobniku KDE.

%prep
%setup -q
%patch0 -p1

rm po/pl.po
install %{SOURCE2} po/pl.po

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__sed} -i -e "s,SUBDIRS = \$(TOPSUBDIRS),SUBDIRS = doc icons po src," Makefile.am
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir}/kde,%{_pixmapsdir},%{_libdir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO 
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/kcheckgmail.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/apps/%{name}
%{_mandir}/man1/kcheckgmail.1*
