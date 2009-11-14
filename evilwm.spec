%define	name	evilwm
%define	version	1.0.1
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://evilwm.sourceforge.net/
Source0:	http://www.6809.org.uk/evilwm/%{name}-%{version}.tar.gz
License:	Public Domain
Group:		Graphical desktop/Other
Summary:	A minimalist window manager for the X Window System
BuildRequires:	nas-devel 
BuildRequires:	lesstif-devel 
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxrandr-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

perl -pi -e 's!^#DEFINES.*-DVDESK.*!DEFINES += -DVDESK!' Makefile

%build
%make CC="gcc $RPM_OPT_FLAGS" LDPATH="-L%{_prefix}/X11R6/%{_lib}"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}

# startfile
%{__cat} > $RPM_BUILD_ROOT%{_bindir}/start%{name} << EOF
#!/bin/sh
exec %{_bindir}/%{name}
EOF

# session file
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d
%{__cat} > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/16%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/16%{name}
%defattr(755,root,root,755)
%{_bindir}/start%{name}
%{_bindir}/%{name}
