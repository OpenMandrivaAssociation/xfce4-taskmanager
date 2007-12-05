%define nversion 0.4.0
%define releasec rc2
%define realversion %{nversion}%{releasec}

Summary:	A small taskmanager for Xfce desktop environment
Name:		xfce4-taskmanager
Version:	%{realversion}
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Source0:	http://goodies.xfce.org/releases/xfce4-taskmanager/%{name}-%{nversion}-%{releasec}.tar.bz2
Source1:	%{name}.desktop
# http://www.xfce.org/images/projects/library.png
Source2:	%{name}.png
BuildRequires:	gdk-pixbuf-devel >= 0.22.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-taskmanager
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
%setup -q -n %{name}-%{nversion}-%{releasec}

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

%find_lang %{name}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/xfce4-taskmanager.png
