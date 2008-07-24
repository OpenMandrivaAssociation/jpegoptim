%define name	jpegoptim
%define version	1.2.2
%define release	 %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utility to optimize jpeg files
Source0:	%{name}-%{version}.tar.bz2
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

