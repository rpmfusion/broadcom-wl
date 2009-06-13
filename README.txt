-------
GENERAL
-------

This is an OFFICAL-RELEASE of Broadcom's IEEE 802.11a/b/g/n hybrid Linux device
driver for use with Broadcom's BCM4311-, BCM4312-, BCM4321-, and BCM4322-based
hardware.

This driver also supports the incorrectly identified BCM4328 chipset which is
actually a BCM4321 or BCM4322 chipset.

-------
LICENSE
-------

You must read the LICENSE.txt file in the docs directory before using this 
software.

--------------------------
INSTALLATION & USAGE NOTES 
--------------------------

This driver conflicts with the Linux community provided driver for Broadcom 
hardware and cannot be used at the same time. It also conflicts with the ssb
driver and ndiswrapper Broadcom windows drivers. 

To overcome these conflicts this package installs the file 
/etc/modprobe.d/broadcom-wl-blacklist.conf which blacklists the following
kernel modules to prevent them from loading:

b43
bcm43xx
ssb
ndiswrapper

If you require to use any of these modules for other installed hardware then 
you will need to comment out the corresponding entry for that module. Note 
that doing so may prevent this driver from functioning.

----------------------------
ISSUES FIXED IN THIS RELEASE
----------------------------

#72138 - SLED11 / Ubuntu 8.04: 43224 fails to associate after 6 hours

----------------------------
KNOWN ISSUES AND LIMITATIONS
----------------------------

#72238 - 20% lower throughput on channels 149, 153, 157, and 161
#72324 - Ubuntu 8.04: cannot ping when Linux STA is IBSS creator with WEP
enabled
#72216 - Ubuntu 8.04: standby/resume with WPA2 and wpa_supplicant causes a
continuous assoc/disassoc loop
         (issue with wpa_supplicant, restarting wpa_supplicant fixes the
issue)

