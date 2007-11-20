%define oname xfce4-taskmanager

Summary:	A small taskmanager for Xfce
Name:		xfce-taskmanager
Version:	0.3.2
Release:	%mkrel 6
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Source0:	http://goodies.xfce.org/releases/xfce4-taskmanager/%{oname}-%{version}.tar.bz2
Source1:	%{oname}.desktop
# http://www.xfce.org/images/projects/library.png
Source2:	%{oname}.png
BuildRequires:	gdk-pixbuf-devel >= 0.22.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_iconsdir}/hicolor/48x48/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/hicolor/48x48/apps

%find_lang %{oname}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/%{oname}.desktop
%{_iconsdir}/hicolor/48x48/apps/xfce4-taskmanager.png
