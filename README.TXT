README.TXT  - 2009-07-17

This is the JFX OpenVPN Client GUI. 

As of this writing, the code is somewhere between what I've called
1.0-alpha2 and what will be 1.0-beta1. 

This README only refers to the GUI, which was written by Rob Lemley.
I have tried to identify any files that I am responsible for with some 
sort of header.

If you're downloading the "source" package, then everything in this
tarball I wrote. If this file is part of a Windows installer or a Mac
Application, then see the README file for that. There's a bunch of
stuff in those downloads that I did not write, and I want to make sure
that the authors of those softwares are given credit where it is due.

This GUI was written because I do not care for the GUI for Windows
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
    definitely don't want to lose any functionality
  - The ability to import existing configs that may be in place from a normal
    OpenVPN installation. Bonus points to import Viscosity configs. It would make
    my day if I can use the same config for all of my clients.
    
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
There is some custom field support in this version. (1.0-beta1) There are a few
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
  - I wrote custom field support while on a plane with no ability to test my code...
    long story, suffice to say I really fucked up my laptop right before this flight
    so things like pyuic4 don't work...

TODO:
In no particular order --
  - Fill out the tray icon menu: add entries for all of the connections, and a submenu for
    those to connect/disconnect/edit properties. 
  - Maybe support connecting to multiple servers at once. Not a high priority.
  - Test and clean up custom field support
