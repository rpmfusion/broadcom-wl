Name:		broadcom-wl
Version:	5.10.27.6
Release:	4%{?dist}
Summary:	Common files for Broadcom 802.11 STA driver
Group:		System Environment/Kernel
License:	Redistributable, no modification permitted
URL:		http://www.broadcom.com/support/802.11/linux_sta.php
Source0:	http://www.broadcom.com/docs/linux_sta/hybrid-portsrc-x86_32_5_10_27_6.tar.gz
Source1:	http://www.broadcom.com/docs/linux_sta/README.txt
Source2:	broadcom-wl-blacklist
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
%config(noreplace) %{_sysconfdir}/modprobe.d/broadcom-wl-blacklist

%changelog
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
