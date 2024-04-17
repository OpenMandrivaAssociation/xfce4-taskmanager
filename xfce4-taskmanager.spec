%define url_ver %(echo %{version} | cut -d . -f 1,2)
%define _disable_rebuild_configure 1

Summary:	A small taskmanager for Xfce desktop environment
Name:		xfce4-taskmanager
Version:	1.5.7
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Source0:	http://archive.xfce.org/src/apps/xfce4-taskmanager/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(libxfce4ui-2) 
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(xmu)
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
%configure \
	--enable-wnck \
	--enable-gtk3 \
	--disable-gtk2

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/actions/xc_crosshair-symbolic.svg
%{_iconsdir}/hicolor/*x*/apps/org.xfce.taskmanager.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.taskmanager.svg
