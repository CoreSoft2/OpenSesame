# guiclient.mak
# Makefile to build the gui client
# This file is meant to run on Windows though mingw32, this the funky filenames

include ../vars.mak

OVPNLIB=OVPN/__init__.py \
    OVPN/clientmgr.py \
    OVPN/config.py \
    OVPN/exception.py \
    OVPN/vpnmgmt.py
    
# The Ui files are updated by Eric, not managed by the Makefile... for now :)
UI=ui/__init__.py \
    ui/appsettings.py \
    ui/Ui_appsettings.py \
    ui/connectiontable.py \
    ui/logging.py \
    ui/Ui_logging.py \
    ui/openvpnclient.py \
    ui/Ui_openvpnclient.py \
    ui/ovpn_rc.py \
    ui/privkeyentry.py \
    ui/Ui_privkeyentry.py \
    ui/properties.py \
    ui/Ui_properties.py \
	ui/customfieldtable.py

TAPFILES=installer/tapinstaller.py installer/installedfiles/tapinstaller.exe.manifest installer/tapinstaller-versioninfo.txt
GUIFILES=openvpnclient.py $(OVPNLIB) $(UI)

$(GUITARGET): $(GUIFILES) installer/gui-versioninfo.txt installer/installedfiles/jfx\ openvpnclient.exe.manifest
	export GUIDIR=$(GUIDIR) && $(PYTHON) $(PYINSTALLER) installer/openvpnclient.spec


# I suppose the tapinstall target should be moved to its own spec file    
$(TAPTARGET): $(TAPFILES)
	export GUIDIR=$(GUIDIR) && $(PYTHON) $(PYINSTALLER) installer/openvpnclient.spec

clean:
	rm -rf installer/build installer/dist installer/tapinstaller.exe installer/JFX\ OpenVPNClient.exe installer/warnpyinstaller.txt installer/warnopenvpnclient.txt *log

all: $(GUITARGET)
#$(TAPTARGET)
