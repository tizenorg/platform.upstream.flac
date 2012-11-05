Name:           flac
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
%ifarch %{ix86}
BuildRequires:  nasm
%endif
Version:        1.2.1
Release:        0
License:        BSD-3-Clause
Summary:        Free Lossless Audio Codec
Url:            http://flac.sourceforge.net/
Group:          Productivity/Multimedia/Sound/Utilities
Source:         %{name}-%{version}.tar.bz2
Patch0:         flac-no-xmms.diff
Patch1:         flac-printf-format-fix.diff
Patch2:         flac-gcc43-fixes.diff
Patch3:         flac-1.2.1-asm.patch
Patch4:         flac-1.2.1-bitreader.patch
Patch5:         flac-ocloexec.patch
Patch6:         flac-visibility.patch
Patch7:         flac-leaks.patch
Patch8:         flac-disable-hidden-visibility-for-ppc.patch
Patch9:         flac-gcc47.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FLAC is an open source lossless audio codec developed by Josh Coalson.

%package -n libflac
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries

%description -n libflac
This package contains the library for FLAC (Free Lossless Audio Codec)
developed by Josh Coalson.

%package -n libflac++
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries

%description -n libflac++
This package contains the C++ library for FLAC (Free Lossless Audio
Codec) developed by Josh Coalson.

%package devel
Summary:        FLAC Library Development Package
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libflac = %{version}
Requires:       libflac = %{version}
Requires:       libstdc++-devel

%description devel
This package contains the files needed to compile programs that use the
FLAC library.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1
%patch4
%patch5
%patch6
%patch7
%patch9 -p1

%build
autoreconf --force --install
%define warn_flags -O3 -W -Wall -Wstrict-prototypes -Wformat-security
export CFLAGS="%{optflags} %{warn_flags}"
export CXXFLAGS="$CFLAGS"
%configure  --disable-thorough-tests --disable-exhaustive-tests\
    --disable-xmms-plugin \
	--disable-static \
	--disable-rpath \
	--with-pic \
    --enable-sse

make %{?_smp_mflags}

%install
%make_install
# documents
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name}-%{version} %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS README COPYING.* %{buildroot}%{_docdir}/%{name}

%post -n libflac -p /sbin/ldconfig

%postun -n libflac -p /sbin/ldconfig

%post -n libflac++ -p /sbin/ldconfig

%postun -n libflac++ -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_mandir}/man*/*

%files -n libflac
%defattr(-, root, root)
%{_libdir}/libFLAC.so.8*

%files -n libflac++
%defattr(-, root, root)
%{_libdir}/libFLAC++.so.6*

%files devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
