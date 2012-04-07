%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A small taskmanager for Xfce desktop environment
Name:		xfce4-taskmanager
Version:	1.0.0
Release:	5
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
