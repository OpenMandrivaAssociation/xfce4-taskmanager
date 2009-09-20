Summary:	A small taskmanager for Xfce desktop environment
Name:		xfce4-taskmanager
Version:	0.4.1
Release:	%mkrel 4
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Source0:	http://goodies.xfce.org/releases/xfce4-taskmanager/%{name}-%{version}.tar.bz2
BuildRequires:	gdk-pixbuf-devel >= 0.22.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
Requires:	xfdesktop
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
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
