%define abi 1.0

Name:           schroedinger
Version:        1.0.0
Release:        1%{?dist}
Summary:        Portable libraries for the high quality Dirac video codec

Group:          System Environment/Libraries
License:        LGPL/MIT/MPL
URL:            http://schrodinger.sourceforge.net/
Source0:	http://diracvideo.schleef.org/download/schroedinger/schroedinger-%{version}.tar.gz
#Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  liboil-devel >= 0.3.13
BuildRequires:  gstreamer-devel >= 0.10
BuildRequires:  gstreamer-plugins-base-devel >= 0.10
BuildRequires:  gtk-doc

%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package devel
Group:          Development/Libraries
Summary:        Development files for schrodinger
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for schrodinger

%package -n gstreamer-plugins-schroedinger
Group:          Applications/Multimedia
Summary:        GStreamer Plugins that implement Dirac video encoding and decoding

%description -n gstreamer-plugins-schroedinger
GStreamer Plugins that implement Dirac video encoding and decoding

%prep
%setup -q

%build
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name \*.la -delete

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING* NEWS TODO
%{_libdir}/libschroedinger-%{abi}.so.*

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/schroedinger-%{abi}
%{_includedir}/schroedinger-%{abi}
%{_libdir}/*.so
%{_libdir}/pkgconfig/schroedinger-%{abi}.pc

%files -n gstreamer-plugins-schroedinger
%defattr(-,root,root,-)
%{_libdir}/gstreamer-0.10/libgstschro.so

%changelog
* Fri Feb 22 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.0-1
- Update to 1.0.0

* Mon Feb 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.9.0-2
- Rebuild for GCC 4.3

* Mon Nov 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.9.0-1
- Update to 0.9.0

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.6.1-3
- Rebuild for selinux ppc32 issue.

* Wed Jun 20 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.6.1-2
- Fix license field
- Add pkgconfig as a requirement for the devel subpackage

* Sun Jun 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.6.1-1
- First version for Fedora
