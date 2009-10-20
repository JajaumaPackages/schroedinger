%define abi 1.0

Name:           schroedinger
Version:        1.0.8
Release:        2%{?dist}
Summary:        Portable libraries for the high quality Dirac video codec

Group:          System Environment/Libraries
# No version is given for the GPL or the LGPL
License:        GPL+ or LGPLv2+ or MIT or MPLv1.1
URL:            http://www.diracvideo.org/
Source0:	http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  liboil-devel >= 0.3.16
BuildRequires:  glew-devel >= 1.5.1
BuildRequires:  gstreamer-devel >= 0.10
BuildRequires:  gstreamer-plugins-base-devel >= 0.10
BuildRequires:  gtk-doc

#Moved to -bad - need to be investigated.
Obsoletes:  gstreamer-plugins-schroedinger < %{version}

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
Summary:        Development files for schroedinger
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:	liboil-devel >= 0.3.16

%description devel
Development files for schroedinger


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
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-%{abi}
%{_libdir}/*.so
%{_libdir}/pkgconfig/schroedinger-%{abi}.pc


%changelog
* Tue Oct 20 2009 kwizart < kwizart at gmail.com > - 1.0.8-2
- Update to 1.0.8
- gstreamer-plugins-schroedinger is now in bad.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.7-1
- Update to 1.0.7

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.5-4
- Fix some typos [BZ#469133]

* Fri Sep 12 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.5-3
- Bump release and rebuild against latest gstreamer-* packages to pick
- up special gstreamer codec provides.

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.5-2
- fix license tag

* Wed Aug 27 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.5-1
- Update to 1.0.5

* Fri Jul  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.3-2
- Devel subpackage needs to require liboil-devel.

* Fri Jun 27 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.3-1
- Update to 1.0.3.
- Update URLs.

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
