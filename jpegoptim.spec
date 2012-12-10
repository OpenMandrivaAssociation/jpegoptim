%define name	jpegoptim
%define version	1.2.3
%define release	 %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utility to optimize jpeg files
Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz
License:	GPL
Group:		Graphics
Url:		http://www.cc.jyu.fi/~tjko/projects.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libjpeg-devel

%description
Provides lossless optimization (based on optimizing the Huffman tables) 
and "lossy" optimization based on setting maximum quality factor.

%prep
%setup -q
%build

%configure

%make

%install

%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYRIGHT README COPYING
%{_bindir}/jpegoptim
%{_mandir}/man1/jpegoptim.1*



%changelog
* Wed Sep 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.3-1mdv2010.0
+ Revision: 451840
- Update to new version 1.2.3

* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2.2-5mdv2010.0
+ Revision: 429646
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.2-4mdv2009.0
+ Revision: 247419
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.2.2-2mdv2008.1
+ Revision: 127413
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import jpegoptim


* Fri Jan 27 2006 Jerome Soyer <saispo@mandriva.org> 1.2.2-2mdk
- Need rebuild

* Sun Aug 08 2004 Couriousous <couriousous@sceen.net> 1.2.2-1mdk
- First Mandrakelinux version
