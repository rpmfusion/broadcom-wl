Name:		broadcom-wl
Version:	5.100.82.38
Release:	1%{?dist}.1
Summary:	Common files for Broadcom 802.11 STA driver
Group:		System Environment/Kernel
License:	Redistributable, no modification permitted
URL:		http://www.broadcom.com/support/802.11/linux_sta.php
Source0:	http://dl.dropbox.com/u/25699833/rpmfusion/sources/broadcom/5_100_82_38/hybrid-portsrc_x86_32-v5_100_82_38.tar.gz
Source1:	http://dl.dropbox.com/u/25699833/rpmfusion/sources/broadcom/5_100_82_38/hybrid-portsrc_x86_64-v5_100_82_38.tar.gz
Source2:	http://dl.dropbox.com/u/25699833/rpmfusion/sources/broadcom/5_100_82_38/README.txt
Source3:	broadcom-wl-blacklist.conf
Source4:	http://dl.dropbox.com/u/25699833/rpmfusion/sources/broadcom/5_100_82_38/bcma.txt
Patch0:		broadcom-wl-5.100.82.38-license.patch
Patch1:		http://dl.dropbox.com/u/25699833/rpmfusion/sources/broadcom/5_100_82_38/5_100_82_38.patch

BuildArch:	noarch
Provides:	wl-kmod-common = %{version}
Requires:	wl-kmod >= %{version}

ExcludeArch:	ppc ppc64

%description
This package contains the license, README.txt and configuration 
files for the Broadcom 802.11 Linux STA Driver for WiFi, a Linux 
device driver for use with Broadcom's BCM4311-, BCM4312-, BCM4313-, 
BCM4321-, BCM4322-, BCM43224-, and BCM43225-, BCM43227- and 
BCM43228-based hardware.

%prep
%setup -q -c
iconv -f iso8859-1 -t UTF8 lib/LICENSE.txt -o lib/LICENSE.txt
sed -i 's/\r$//' lib/LICENSE.txt
cp -p %{SOURCE2} %{SOURCE4} .
chmod 644 lib/LICENSE.txt README.txt bcma.txt
%patch0 -p1 -b .license
%patch1 -p0 -b .init_MUTEX

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/modprobe.d/
install -p -m0644 %{SOURCE3} ${RPM_BUILD_ROOT}/%{_sysconfdir}/modprobe.d/ 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc lib/LICENSE.txt README.txt bcma.txt
%config(noreplace) %{_sysconfdir}/modprobe.d/broadcom-wl-blacklist.conf

%changelog
* Sat Nov 05 2011 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.38-1.1
- Rebuilt for F-15

* Fri Nov 04 2011 Nicolas Vieville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.38-1
- Updated version to 5.100.82.38

* Tue Feb 01 2011 Chris Nolan <chris@cenolan.com> - 5.60.48.36
- updated version to 5.100.82.38

* Mon Feb 22 2010 Chris Nolan <chris@cenolan.com> - 5.60.48.36-1
- updated version to 5.60.48.36

* Sat Sep 19 2009 Chris Nolan <chris@cenolan.com> - 5.10.91.9.3
- updated to 5.10.91.9.3

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 5.10.79.10-2
- rebuild for new F11 features

* Sun Mar 08 2009 Chris Nolan <chris@cenolan.com> - 5.10.79.10-1
- update version to 5.10.79.10

* Sun Feb 01 2009 Chris Nolan <chris@cenolan.com> - 5.10.27.14-1
- update version to 5.10.27.14

* Sun Jan 04 2009 Chris Nolan <chris@cenolan.com> - 5.10.27.12-1
- Update version to 5.10.27.12

* Wed Dec 31 2008 Chris Nolan <chris@cenolan.com> 5.10.27.11-1
- Update version to 5.10.27.11

* Sat Dec 20 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 5.10.27.6-4
- ExcludeArch ppc, ppc64

* Fri Nov 07 2008 Chris Nolan <chris@cenolan.com> 5.10.27.6-3
- Updated README.txt file
- Cleaned up spec file

* Sun Nov 02 2008 Chris Nolan <chris@cenolan.com> 5.10.27.6-2
- Added README.txt file
- Added /etc/modprobe.d/broadcom-wl-blacklist

* Thu Oct 30 2008 Chris Nolan <chris@cenolan.com> 5.10.27.6-1
- Initial Build
