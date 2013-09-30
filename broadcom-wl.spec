Name:       broadcom-wl
Version:    6.30.223.141
Release:    2%{?dist}
Summary:    Common files for Broadcom 802.11 STA driver
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        http://www.broadcom.com/support/802.11/linux_sta.php
Source0:    http://www.broadcom.com/docs/linux_sta/hybrid-v35-nodebug-pcoem-6_30_223_141.tar.gz
Source1:    http://www.broadcom.com/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-6_30_223_141.tar.gz
Source2:    http://www.broadcom.com/docs/linux_sta/README.txt
Source3:    broadcom-wl-blacklist.conf
Source4:    20-wl.conf
Source5:    api
Source6:    fedora.readme
Patch0:     broadcom-wl-001_license.patch

BuildArch:  noarch
Provides:   wl-kmod-common = %{version}
Requires:   wl-kmod >= %{version}

ExcludeArch:    ppc ppc64

%description
This package contains the license, README.txt and configuration 
files for the Broadcom 802.11 Linux STA Driver for WiFi, a Linux 
device driver for use with Broadcom's BCM4311-, BCM4312-, BCM4313-, 
BCM4321-, BCM4322-, BCM43142-, BCM43224-, BCM43225-, BCM43227-, 
BCM43228-, BCM4331-, BCM4360 and -BCM4352- based hardware.

%prep
%setup -q -c
iconv -f iso8859-1 -t UTF8 lib/LICENSE.txt -o lib/LICENSE.txt
sed -i 's/\r$//' lib/LICENSE.txt
cp -p %{SOURCE2} .
cp -p %{SOURCE6} .
chmod 644 lib/LICENSE.txt README.txt fedora.readme
%patch0 -p1 -b .license

%build
echo "Nothing to build."

%install
rm -rf $RPM_BUILD_ROOT
install    -m 0755 -d         $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d/
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d/
install    -m 0755 -d         ${RPM_BUILD_ROOT}%{_sysconfdir}/dracut.conf.d/
install -p -m 0644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/dracut.conf.d/
install    -m 0755 -d         ${RPM_BUILD_ROOT}%{_sysconfdir}/akmods/akmod-wl/
install -p -m 0644 %{SOURCE5} ${RPM_BUILD_ROOT}%{_sysconfdir}/akmods/akmod-wl/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc lib/LICENSE.txt README.txt fedora.readme
%config(noreplace) %{_prefix}/lib/modprobe.d/broadcom-wl-blacklist.conf
%config(noreplace) %{_sysconfdir}/dracut.conf.d/20-wl.conf
%config(noreplace) %{_sysconfdir}/akmods/akmod-wl/api

%changelog
* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.30.223.141-2
- Rebuilt

* Sat Sep 14 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 6.30.223.141-1
- Upstream update to 6.30.223.141

* Mon Jan 21 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.112-4
- move broadcom-wl-blacklist.conf to %%{_prefix}/lib/modprobe.d/ since new dracut in F-18
- install section cleaned-up

* Wed Nov 21 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.112-3
- Added /etc/dracut.conf.d/20-wl.conf to workaround #2526
- Added /etc/akmods/akmod-wl/api to workaround #2548 #2562
- fedora.readme added to explain usage of the above

* Thu Apr 19 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.112-2
- Rebuilt to correct release number

* Thu Apr 19 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.112-1
- Rebuilt for rawhide

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.100.82.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Nicolas Vieville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.112-1
- Updated version to 5.100.82.112

* Sat Nov 05 2011 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 5.100.82.38-1.1
- Rebuilt for F-16

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
