VirtualBox Guest Additions Driver for OS/2

Prerequisites:
- the generic VESA gradd driver is being used (gengradd)

Updated installation instructions:
- boot to the OS/2 command prompt (alt-f1 while the white blob is displayed during early boot, then f2)
- copy all files into the directory C:\VBoxAdd
- make a backup copy of C:\os2\dll\gengradd.dll
- copy our gengradd.dll to C:\os2\dll
- copy libc06*.dll to C:\os2\dll
- comment out the 'device=C:\os2\boot\mouse.sys' line in C:\config.sys (put 'rem' in front)
- append 'device=C:\VBoxAdd\vboxguest.sys' to C:\config.sys
- append 'device=C:\VBoxAdd\vboxmouse.sys' to C:\config.sys
- append 'ifs=C:\VBoxAdd\vboxsf.ifs' to C:\config.sys
- append C:\VBoxAdd to PATH if you want to use VBoxControl.exe and shared folders.
- add  'C:\VBoxAdd\VBoxService.exe' to the start of C:\startup.cmd
- reboot

Alternative:
- Run the barebone VBoxOs2AdditionsInstall.exe installer (main audience is
  unattended installation).  Please check out the --help text.
  Remember to pass it --do-install for the actual installation run.


Shared folders
--------------

The shared folders are brand new in 6.0 and considered beta quality.

To attach a shared folder to a drive letter:
        VBoxControl sharedfolder use <drive> <shared-folder-name>

To detach a shared folder from a drive:
        VBoxControl sharedfolder unuse <drive>

To see available shared folders (any guest type):
        VBoxControl sharedfolder list

The shared folders are accessible via UNC too:
        dir \\vboxsf\folder\
    or: dir \\vboxsvr\folder\
    or: dir \\vboxsrv\folder\

The VBoxService can also attach and detach shared folders to/from drive
letters, if you check the 'Auto-Mount' flag in the config (host GUI).

