Summary:	Utility to optimize JPEG image files
Name:		jpegoptim
Version:	1.3.0
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://www.kokkonen.net/tjko/projects.html
Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz
BuildRequires:	jpeg-devel

%description
Provides lossless optimization (based on optimizing the Huffman tables)
and "lossy" optimization based on setting the maximum quality factor.

%files
%doc COPYRIGHT README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall


