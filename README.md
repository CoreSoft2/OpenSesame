# UPDATE UPDATE UPDATE UPDATE

## 2018-04-06

April 2015 - After almost 7 year's I'm reviving this project. The short
version is that I have a need to connect a Windows box to an OpenVPN
service, and I still don't like the one from OpenVPN.

Change-wise, first up is to revert the PySide changes. Last I checked,
PySide development is lagging, so for now I suspect it's best to just
stick with PyQt. I may refactor again to support one of the PyQt/PySide
compatibility libraries that have popped up recently, but we'll see.

There's now a "dev" branch. All development will take place there. I'll
keep "master" as a stable branch, though honestly it may not even work.

Platform support: I only plan to support Windows; that's my use case.
NetworkManager on Linux works for me, and I don't use MacOS. But it's
Qt, so supporting Linux or Mac shouldn't be too bad if someone else 
wants to put the effort into it.



This is OpenSesame. 

I'm calling this release Beta-1, 0.9.1
Beta-2 will be 0.9.2, etc.


This README only refers OpenSesame, which was written by Rob Lemley.
I have tried to identify any files that I am responsible for with some 
sort of header.

If you're downloading the "source" package, then everything in this
tarball I wrote. If this file is part of a Windows installer or a Mac
Application (vaporware), then see the README file for that. There's a bunch of
stuff in those downloads that I did not write, and I want to make sure
that the authors of those softwares are given credit where it is due.

OpenSesame was written because I do not care for the GUI for Windows
that comes with OpenVPN. My employer uses OpenVPN extensively
for various purposes. Most of our employees use the VPN to work
remotely. For the Mac users, there's a wonderful application called
Viscosity that works great. Too bad it's a Mac-only app. :) Our poor
Windows users (not that we really have that many... but they exist)
have to use that GUI that comes with OpenVPN. No offense to the
author, but it's just a little too limited in its functionality for our users.
In addition, it is nearly impossible to use effectively on a multi-user 
machine. Believe me, I've tried... never again. :)

What I'm setting out to fix:
  - a GUI interface to the configuration that a regular Joe-user can make
    changes to when the evil BOFH makes changes to the server config that
    require changes on the client side
  - a more informative UI... something that you can see is running, can hide
    when you want, and gives you good feedback on what's going on
  - Something that has potential to be cross-platform, even if it's not right
    away
  - Something Viscosity doesn't have that I want... the ability to change your
    certificate passphrase. The Windows GUI from openvpn.net has this... I
    definitely don't want to lose any functionality (not implemented)
  - The ability to import existing configs that may be in place from a normal
    OpenVPN installation. Bonus points to import Viscosity configs. It would make
    my day if I can use the same config for all of my clients. (sorta...)
    
As of this writing, this thing definitely works on Windows. So far so good on
Linux. It probably needs some work to be usable on Mac. My main target is
Windows anyway. Linux would be nice, Mac support is just bonus points, as
we have Viscosity for Mac, and it works quite nicely.

HOW TO USE:
Here's the general idea --
  - Create or import a configuration. This will create a directory in the JFX config dir
    that has the config, and any certificates you need.
  - Select the configuration in the GUI, and press "Connect". From here, you can view
    the log window to see whats going on behind the scenes, or you can just wait for
    the status to say "Connected". 
  - Once connected, use the VPN as usual. To disconnect, press the "Disconnect" button.
  
CUSTOM FIELD SUPPORT:
There is some custom field support in this version. (0.9.0) There are a few
limitations/bugs that probably need to be addressed before 1.0-Release...
  - Custom fields need to be "supported". Currently, this is a list defined in the
    depths of config.py. As of this writing, that list is empty... so custom fields
    are not that useful. :) I'm debating whether to move that list to a file that's
    read at startup time or what. If you're running from source like you might
    on Linux, it's not a big deal to hack config.py and add more supported custom
    fields, but on a compiled platform like Windows, it won't be doable. 
  - I don't make any effort to check the syntax of custom fields. They're meant
    for ADVANCED users... like your IT staff to set. I figure if the user screws up their
    config by setting a custom field that OpenVPN doesn't like it's their own bloody
    fault. That may be a bit harsh for the average Windows user... I probably need
    to make some effort to at least find out what custom field is messing up 
    OpenVPN, if that's even doable. There's a TODO item someplace for this.
p

TODO:
In no particular order --
  - Ability to change SSL key passphrases... This is a royal PITA...
  - Fill out the tray icon menu: add entries for all of the connections, and a submenu for
    those to connect/disconnect/edit properties. 
  - Maybe support connecting to multiple servers at once. Not a high priority.
  - Test and clean up custom field support -- seems to work... 9/3/09
  - support auth plugins clientside (username/password dialog)
  - Keep an eye on PySide, maybe switch to that -- it doesn't work on Windows yet :(
  - support different certificate configurations... like shared-key setups... pkcs11...
  - add field to display to show VPN IP when connected
  - fix crashes when connection dies unexpectedly
  - make sure theres no openvpn process hanging out if we crash
  - if conn dies, make sure the gui gets reset
