Summary:	KDE systray application to check your Gmail
Summary(pl.UTF-8):	Aplikacja do sprawdzania Gmaila w zasobniku KDE
Name:		kcheckgmail
Version:	0.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/kcheckgmail/%{name}-%{version}.tar.bz2
# Source0-md5:	12d375119d7048d6649532b0b0cae32b
Patch0:		%{name}-firefox-name.patch
Patch1:		%{name}-desktop.patch
URL:		http://kcheckgmail.sourceforge.net/
BuildRequires:	cmake >= 2.4.5
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE systray application to check your Gmail.

%description -l pl.UTF-8
Aplikacja do sprawdzania Gmaila w zasobniku KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake  \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"

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
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/kcheckgmail
%{_desktopdir}/kde4/kcheckgmail.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/apps/%{name}
%{_mandir}/man1/kcheckgmail.1*
