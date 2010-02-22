Broadcom Linux hybrid wireless driver

DISCLAIMER
----------
This is an Official Release of Broadcom's hybrid Linux driver for use with 
Broadcom based hardware.

LICENSE
-------
You must read the LICENSE.txt file in the docs directory before using this 
software.

ABOUT THIS RELEASE
-------------------
This is a rollup release.  It includes and deprecates all previous releases
and patches.  At the time of release there are no existing patches for this
release from Broadcom.

SUPPORTED DEVICES
-----------------
The cards with the following PCI Device IDs are supported with this driver.
Both Broadcom and and Dell product names are described.  Cards not listed here
may also work.

	   BRCM		    PCI		  PCI		  Dell
	  Product Name	  Vendor ID	Device ID	Product ID
          -------------	 ----------	---------   	-----------
          4311 2.4 Ghz	    0x14e4	0x4311  	Dell 1390
          4311 Dualband	    0x14e4	0x4312  	Dell 1490
          4311 5 Ghz	    0x14e4    	0x4313  	
          4312 2.4 Ghz	    0x14e4	0x4315  	Dell 1395
          4313 2.4 Ghz	    0x14e4	0x4727 		Dell 1501
          4321 Dualband	    0x14e4	0x4328  	Dell 1505
          4321 Dualband	    0x14e4	0x4328  	Dell 1500
          4321 2.4 Ghz	    0x14e4	0x4329  	
          4321 5 Ghz        0x14e4	0x432a  	
          4322 	Dualband    0x14e4	0x432b  	Dell 1510
          4322 2.4 Ghz      0x14e4 	0x432c  	
          4322 5 Ghz        0x14e4 	0x432d  	
          43224 Dualband    0x14e4	0x4353  	Dell 1520
          43225 2.4 Ghz     0x14e4	0x4357  	

To find the Device ID's of Broadcom cards on your machines do:
# lspci -n | grep 14e4

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

TX POWER EXPLAINED
------------------
'iwconfig eth1 txpower' & 'iwlist eth1 txpower' set and get the drivers 
user-requested transmit power level. This can go up to 32 dbm and allows
the user to lower the tx power to levels below the regulatory limit.
Internally, the actual tx power is always kept within regulatory limits
no matter what the user request is set to.

WHAT'S NEW IN THIS RELEASE
----------------------------
+ Supports up to linux kernel 2.6.31. 2.6.32 support is there also but 
not tested (although reports from users suggests it works fine.)
+ Supports hidden networks
+ Supports rfkill in kernels <  2.6.31
+ Setting power level via 'iwconfig eth1 txpower X' now operational
+ Support for 4313
+ Additional channels in both 2.4 and 5 Ghz bands.
+ Fixed issue with tkip group keys that caused this message to repeat often:
	TKIP: RX tkey->key_idx=2 frame keyidx=1 priv=ffff8800cf80e840
+ Following fixes
    Issue #72216 - Ubuntu 8.04: standby/resume with WPA2 and wpa_supplicant causes
                               a continuous assoc/disassoc loop (issue in 2.6.24 kernel)
    Issue #72324 - Ubuntu 8.04: cannot ping when Linux STA is IBSS creator with WEP
    Issue #76739 - Ubuntu 9.04: unable to connect to hidden network after stdby/resume
    Issue #80392 - S4 resume hang with SuSE SLED 11 and 43225
    Issue #80792 - LSTA is not able to associate to AP with transition from AES to TKIP encryption

KNOWN ISSUES AND LIMITATIONS
----------------------------
#72238 - 20% lower throughput on channels 149, 153, 157, and 161
#76743 - Ubuntu9.04: Network manager displays n/w's with radio disabled
#76793 - Ubuntu9.04: STA fails to create IBSS network in 5 Ghz band
#81392 - Unable to transfer data over ad-hoc network created by NetworkManager (iwconfig OK)
#81452 - STA unable to associate to AP when PEAPv1-MSCHAPv2 authentication is used
