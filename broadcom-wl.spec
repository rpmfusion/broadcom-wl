%if 0%{?rhel} > 6 || 0%{?fedora}
 # The common usage uses /usr directory, even if it's not conforming to
 # Fedora Packaging Guidelines, as well kmod and dracut packages, see:
 # https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Configuration_files
 %global        _modprobe_d         %{_prefix}/lib/modprobe.d
 %global        _dracut_conf_d      %{_prefix}/lib/dracut/dracut.conf.d
 %global        _nmlibdir_conf_d    %{_prefix}/lib/NetworkManager/conf.d
%else #rhel <= 6
 %global        _modprobe_d         %{_sysconfdir}/modprobe.d
 %global        _dracut_conf_d      %{_sysconfdir}/dracut.conf.d
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
 %bcond_without python3
%else
 %bcond_with python3
%endif

Name:       broadcom-wl
Version:    6.30.223.271
Release:    13%{?dist}
Summary:    Common files for Broadcom 802.11 STA driver
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://www.broadcom.com/support/download-search?pg=&pf=Wireless+LAN/Bluetooth+Combo
Source0:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35-nodebug-pcoem-6_30_223_271.tar.gz
Source1:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-6_30_223_271.tar.gz
Source2:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/README_6.30.223.271.txt
Source3:    broadcom-wl-blacklist.conf
Source4:    20-wl.conf
Source5:    api
Source6:    fedora.readme
Source7:    com.broadcom.wireless.hybrid.driver.metainfo.xml
Source8:    generate-modalias-metadata.py
Source9:    90-broadcom-wl.conf

BuildArch:  noarch
Provides:   wl-kmod-common = %{?epoch}:%{version}
Requires:   wl-kmod >= %{?epoch}:%{version}

ExcludeArch:    ppc ppc64

%if 0%{?rhel} > 6 || 0%{?fedora} >= 25
# AppStream metadata generation
%if %{with python3}
BuildRequires:    python3
%else
BuildRequires:    python
%endif
BuildRequires:    libappstream-glib
%endif

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
chmod 644 lib/LICENSE.txt README_6.30.223.271.txt fedora.readme

%build
echo "Nothing to build."

%install
install    -m 0755 -d         %{buildroot}%{_modprobe_d}
install -p -m 0644 %{SOURCE3} %{buildroot}%{_modprobe_d}/
install    -m 0755 -d         %{buildroot}%{_dracut_conf_d}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_dracut_conf_d}/
install    -m 0755 -d         %{buildroot}%{_sysconfdir}/akmods/akmod-wl/
install -p -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/akmods/akmod-wl/
%if 0%{?rhel} > 6 || 0%{?fedora} >= 25
install    -m 0755 -d         %{buildroot}%{_nmlibdir_conf_d}/
install -p -m 0644 %{SOURCE9} %{buildroot}%{_nmlibdir_conf_d}/
# install AppData and add modalias provides
install    -m 0755 -d         %{buildroot}%{_metainfodir}/
install -p -m 0644 %{SOURCE7} %{buildroot}%{_metainfodir}/
fn=%{buildroot}%{_metainfodir}/com.broadcom.wireless.hybrid.driver.metainfo.xml
# As appstream-util deletes all comments in the metainfo.xml file, the
# copyright must be saved and re-written to the resulting file.
copyright_string=$(grep Copyright ${fn})
%if %{with python3}
python3 %{SOURCE8} README_6.30.223.271.txt "SUPPORTED DEVICES" | xargs appstream-util add-provide ${fn} modalias
%else
python %{SOURCE8} README_6.30.223.271.txt "SUPPORTED DEVICES" | xargs appstream-util add-provide ${fn} modalias
%endif
appstream-util validate-relax --nonet ${fn}
grep -q Copyright ${fn} >/dev/null || sed -i "s%\(^<?xml.*$\)%\1\n${copyright_string}%" ${fn}
%endif

%files
%doc README_6.30.223.271.txt fedora.readme
# Caution - testing rhel or fedora value with < or <= operators is risky,
# while using > or >= operators seems to give the right result.
# See 07/03/2017 update on http://backreference.org/2011/09/17/some-tips-on-rpm-conditional-macros/
%if 0%{?rhel} > 6 || 0%{?fedora} > 20
%license lib/LICENSE.txt
%else
%doc lib/LICENSE.txt
%endif
%if 0%{?rhel} > 6 || 0%{?fedora} >= 25
%{_metainfodir}/com.broadcom.wireless.hybrid.driver.metainfo.xml
%config %{_nmlibdir_conf_d}/90-broadcom-wl.conf
%endif
%config(noreplace) %{_modprobe_d}/broadcom-wl-blacklist.conf
%config(noreplace) %{_dracut_conf_d}/20-wl.conf
%config(noreplace) %{_sysconfdir}/akmods/akmod-wl/api

%changelog
* Wed Oct 16 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 6.30.223.271-13
- Updated URLs to new Broadcom WEB site

* Tue Sep 24 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 6.30.223.271-12
- Workaround RHBZ#1703745 and RFBZ#5245 - Disable NetworkManager scan 
  with randomized MAC address and added appropriated section in 
  fedora.readme file
- fedora.readme clean-up
- Use %%{_metainfodir} macro in spec file

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.223.271-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 06 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 6.30.223.271-10
- improve SPEC file for RHEL 6.x and 7.x AppStream Metadata

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.223.271-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.223.271-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 6.30.223.271-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 6.30.223.271-6
- Move AppStream Metadata to /usr/share/metainfo directory
- Added appstream-util validate-relax to conform with f28 packaging guidelines

* Wed Apr 18 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 6.30.223.271-5
- Added AppStream Metadata
- Update new Broadcom upstream URLs in SPEC file
- Cleanup and rework SPEC file for RHEL 6.x and 7.x

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 6.30.223.271-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 6.30.223.271-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 6.30.223.271-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 14 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 6.30.223.271-1
- Upstream update to 6.30.223.271

* Wed May 20 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 6.30.223.248-3
- Update new Broadcom upstream URLs in SPEC file
- Update to move license file to %%license
- install section cleaned-up

* Sat Dec 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 6.30.223.248-2
- Rebuilt for f21

* Tue Jul 15 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 6.30.223.248-1
- Upstream update to 6.30.223.248

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
