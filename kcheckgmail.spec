Summary:	KDE systray application to check your Gmail
Summary(pl):	Aplikacja do sprawdzania Gmaila w zasobniku KDE
Name:		kcheckgmail
Version:	0.5.2
Release:	0.2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kcheckgmail/%{name}-%{version}.tar.bz2
# Source0-md5:	be004ebb1d8f3d951cb4fb7bffccab34
URL:		http://kcheckgmail.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE systray application to check your Gmail.

%description -l pl
Aplikacja do sprawdzania Gmaila w zasobniku KDE.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/kcheckgmail.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/apps/%{name}
