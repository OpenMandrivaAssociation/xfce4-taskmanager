%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A small taskmanager for Xfce desktop environment
Name:		xfce4-taskmanager
Version:	1.0.0
Release:	6
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Source0:	http://archive.xfce.org/src/apps/xfce4-taskmanager/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libwnck-devel
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)
Requires:	xfdesktop
Obsoletes:	xfce-taskmanager

%description
xfce-taskmanager is a small taskmanager based on the Xfce libraries.

Features:
    * Lists up all tasks of the running System
    * Provides sending signals to tasks:
    - STOP
    - CONT
    - TERM
    - KILL

%prep
%setup -q

%build
%configure2_5x \
	--enable-wnck

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.0-5
+ Revision: 789645
- rebuild
- spec file clean

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.0-4
+ Revision: 633053
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.0-3mdv2011.0
+ Revision: 579674
- rebuild for new xfce 4.7.0
- disable option with-skel

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.0-1mdv2011.0
+ Revision: 553884
- update to new version 1.0.0
- adjust buildrequires

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.1-5mdv2010.1
+ Revision: 543313
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 1:0.4.1-4mdv2010.0
+ Revision: 446137
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.1-3mdv2009.1
+ Revision: 349231
- rebuild whole xfce

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.1-2mdv2009.1
+ Revision: 294986
- rebuild for new Xfce4.6 beta1

* Tue Sep 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.1-1mdv2009.0
+ Revision: 285094
- update to new version 0.4.1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1:0.4.0-2mdv2009.0
+ Revision: 269795
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.0-1mdv2009.0
+ Revision: 208959
- new version (yes 0.4.0 > 0.4.1, anyways don't tknow how but from where came 0.4.1 version?)
- drop desktop file, as it was mergen upstream

* Sat Feb 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-2mdv2008.1
+ Revision: 174095
- use icon shipped with xfdesktop

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 119338
- Fix tarball
- Bump Version
- Bump Version
- New release 0.4.0

* Wed Dec 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.0rc2-1mdv2008.1
+ Revision: 115768
- New release to fix old bugs

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-6mdv2008.1
+ Revision: 110637
- new license policy
- do not package COPYING and NEWS, add ChangeLog instead
- use upstream tarball name

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 0.3.2-6mdv2008.0
+ Revision: 36217
- rebuild with correct optflags

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - correct attribute bits

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-4mdv2008.0
+ Revision: 34709
- adjust desktop file

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-3mdv2008.0
+ Revision: 34562
- add desktop file
- add icon (stolen from the xfce site :)

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-2mdv2008.0
+ Revision: 30480
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2008.0
+ Revision: 30225
- new version

