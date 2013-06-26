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
Group:          Multimedia/Audio
Source:         %{name}-%{version}.tar.bz2

%description
FLAC is an open source lossless audio codec developed by Josh Coalson.

%package -n libflac
Summary:        Free Lossless Audio Codec Library

%description -n libflac
This package contains the library for FLAC (Free Lossless Audio Codec)
developed by Josh Coalson.

%package -n libflac++
Summary:        Free Lossless Audio Codec Library

%description -n libflac++
This package contains the C++ library for FLAC (Free Lossless Audio
Codec) developed by Josh Coalson.

%package devel
Summary:        FLAC Library Development Package
Requires:       glibc-devel
Requires:       libflac = %{version}
Requires:       libflac = %{version}
Requires:       libstdc++-devel

%description devel
This package contains the files needed to compile programs that use the
FLAC library.

%prep
%setup -q

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
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%post -n libflac -p /sbin/ldconfig

%postun -n libflac -p /sbin/ldconfig

%post -n libflac++ -p /sbin/ldconfig

%postun -n libflac++ -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license  COPYING.*
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
