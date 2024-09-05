#
# spec file for package xdiskusage
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Note that this is NOT a relocatable package
%define prefix          /usr
%define bindir          /usr/bin
%define mandir          /usr/share/man
%define tmppath         /tmp

Summary:        Graphically displays the amount of disk space used by each subdirectory
License:        GPL-2.0
Group:          Applications/System

Name:           xdiskusage
Version:        1.60
Release:        1
Source:         %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://xdiskusage.sourceforge.net/
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
#BuildRequires:  fluid

%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  mesa-libGL-devel
%endif
%if 0%{?suse_version}
BuildRequires:  Mesa-devel
BuildRequires:  xorg-x11-devel
%endif
%if 0%{?mandriva_version}
%ifarch x86_64
BuildRequires:  lib64mesagl1-devel
BuildRequires:  lib64x11_6-devel
BuildRequires:  lib64xext6-devel
BuildRequires:  lib64xinerama1-devel
%else
BuildRequires:  libmesagl1-devel
BuildRequires:  libx11_6-devel
BuildRequires:  libxext6-devel
BuildRequires:  libxinerama1-devel
%endif
%endif

%description
xdiskusage is a user-friendly program to show you what is using 
up all your disk space. It is based on the design of xdu 
written by Phillip C. Dykstra. Changes have been made so it runs 
"du" for you, and can display the free space left on the disk, 
and produce a PostScript version of the display.

%global debug_package %{nil}

%prep
%setup -q

%build
export CXXFLAGS="$RPM_OPT_FLAGS"
export CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{bindir} $RPM_BUILD_ROOT/%{mandir}/man1
make prefix=$RPM_BUILD_ROOT/%{prefix} \
	mandir=$RPM_BUILD_ROOT/%{mandir} install

%files
%defattr(-,root,root)
%doc README
%{bindir}/*
%doc %attr(0644,root,root) %{mandir}/man1/*

%changelog
* Thu Sep 5 2024 John Beranek <jberanek@users.sf.net>
- v1.60 from upstream.
