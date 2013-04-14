%define	name	evilwm
%define	version	1.0.1
%define	release	5
%define debug_package %{nil}

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2011.0
+ Revision: 664153
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 605108
- rebuild

* Sat Nov 14 2009 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 465989
- new version 1.0.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-5mdv2010.0
+ Revision: 424391
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2009.0
+ Revision: 220730
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2008.1
+ Revision: 149702
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-2mdv2008.0
+ Revision: 53331
- clean buildrequires, rebuild with new lesstif

* Sun Jul 08 2007 Nicolas Vigier <nvigier@mandriva.com> 1.0.0-1mdv2008.0
+ Revision: 49646
- new version
- Import evilwm



* Thu Apr 27 2006 Lenny Cartier <lenny@mandriva.com> 0.99.25-1mdk
- 0.99.25

* Wed Apr 26 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.99.24-1mdk
- 0.99.24
- add url to source

* Wed Feb 01 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.99.22-2mdk
- lib64 fix
- fix buildrequires

* Tue Jan 31 2006 Lenny Cartier <lenny@mandriva.com> 0.99.22-1mdk
- 0.99.22

* Fri Jun 03 2005 Eskild Hustvedt <eskild@mandriva.org> 0.99.18-2mdk
- Make rpmlint happy

* Fri Jun 03 2005 Eskild Hustvedt <eskild@mandriva.org> 0.99.18-1mdk
- New version 0.99.18
- %%mkrel

* Mon Nov 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.99.17-3mdk
- rebuild

* Thu Oct 30 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.99.17-2mdk
- enable virtual desktop support

* Thu Oct 30 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.99.17-1mdk
- 0.99.17
- fix buildrequires (lib64..)

* Fri Sep 05 2003 Marcel Pol <mpol@gmx.net> 0.99.14-2mdk
- buildrequires

* Sun Jun 01 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.99.14-1mdk
- initial mdk release
