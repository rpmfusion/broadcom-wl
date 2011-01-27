Name:		broadcom-wl
Version:	5.100.82.38
Release:	1%{?dist}
Summary:	Common files for Broadcom 802.11 STA driver
Group:		System Environment/Kernel
License:	Redistributable, no modification permitted
URL:		http://www.broadcom.com/support/802.11/linux_sta.php
Source0:	http://www.broadcom.com/docs/linux_sta/hybrid-portsrc_x86_32-v5_100_82_38.tar.gz
Source1:	http://www.broadcom.com/docs/linux_sta/README.txt
Source2:	broadcom-wl-blacklist.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Provides:	wl-kmod-common = %{version}
Requires:	wl-kmod >= %{version}

ExcludeArch:    ppc ppc64

%description
This package contains the license, readme and configuration files
for the Broadcom 802.11 Linux STA Driver for WiFi, a linux device 
driver for use with Broadcom's BCM4311-, BCM4312-, BCM4321-, and 
BCM4322-based hardware.

%prep
%setup -q -c
iconv -f iso8859-1 -t UTF8 lib/LICENSE.txt -o lib/LICENSE.txt
sed -i 's/\r$//' lib/LICENSE.txt
cp -p %{SOURCE1} .
chmod 644 lib/LICENSE.txt README.txt

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/modprobe.d/
install -p -m0644 %{SOURCE2} ${RPM_BUILD_ROOT}/%{_sysconfdir}/modprobe.d/ 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc lib/LICENSE.txt README.txt
%config(noreplace) %{_sysconfdir}/modprobe.d/broadcom-wl-blacklist.conf

%changelog
* Thu Jan 27 2011 Chris Nolan <chris@cenolan.com> - 5.100.82.38
- updated version to  5.100.82.38

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
