Summary:	Utility to optimize JPEG image files
Name:		jpegoptim
Version:	1.5.6
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://www.kokkonen.net/tjko/projects.html
Source0:	https://github.com/tjko/jpegoptim/releases/download/v%{version}/jpegoptim-%{version}.tar.gz

BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slibtool

%description
Provides lossless optimization (based on optimizing the Huffman tables) and
"lossy" optimization based on setting the maximum quality factor.

%prep
%autosetup -p1

%conf
# Some versions of autoconf seem to set HOST_TYPE. Ours doesn't
export CPPFLAGS='%{optflags} -DHOST_TYPE=\"%{_target_platform}\"'
%configure

%build
%make_build

%install
%make_install

%files
%doc COPYRIGHT README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
