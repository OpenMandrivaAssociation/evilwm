%define debug_package %{nil}

Summary:	A minimalist window manager for the X Window System
Name:		evilwm
Version:	1.1.0
Release:	1
License:	Public Domain
Group:		Graphical desktop/Other
Url:		http://evilwm.sourceforge.net/
Source0:	http://www.6809.org.uk/evilwm/%{name}-%{version}.tar.gz

BuildRequires:	lesstif-devel 
BuildRequires:	nas-devel 
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)

%description
evilwm is a minimalist window manager for the X Window System.

The name evil came from Stuart 'Stuii' Ford, who thinks that any software
I use must be evil and masochistic.  In reality, this window manager is
clean and easy to use.

FEATURES

 * No window decorations apart from a simple 1 pixel border.
 * No icons.
 * Good keyboard control, including repositioning and maximise toggles.
 * Solid window drags (compile time option - may be slow on old machines).
 * Virtual desktops.
 * Small binary size (even with everything turned on).

%prep
%setup -q
sed -i -e 's!^#DEFINES.*-DVDESK.*!DEFINES += -DVDESK!' Makefile

%build
%make CC="gcc $RPM_OPT_FLAGS" LDPATH="-L%{_prefix}/X11R6/%{_lib}"

%install
%makeinstall_std

# startfile
cat > %{buildroot}%{_bindir}/start%{name} << EOF
#!/bin/sh
exec %{_bindir}/%{name}
EOF

# session file
install -d %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/16%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

%files
%doc README ChangeLog TODO
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/16%{name}
%{_bindir}/start%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


