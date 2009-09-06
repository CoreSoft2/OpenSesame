# OVPN/customfields.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

# This is just a list of allowed custom fields. It is manually maintained for now
# by hacking up the output from openvpn --help.

ALLOWEDCFS = [
'local',
'remote',
'remote-random',
'connect-retry',
'connect-timeout',
'connect-retry-max',
'auto-proxy',
'http-proxy',
'http-proxy',
'http-proxy-retry',
'http-proxy-timeout',
'http-proxy-option',
'socks-proxy',
'socks-proxy-retry',
'resolv-retry',
'float',
'ipchange',
'dev-node',
'tun-ipv6',
'ifconfig',
'ifconfig-noexec',
'ifconfig-nowarn',
'route',
'route-gateway',
'route-metric',
'route-delay',
'route-up',
'route-noexec',
'route-nopull',
'allow-pull-fqdn',
'redirect-gateway',
'redirect-private',
'setenv',
'script-security',
'shaper',
'keepalive',
'inactive',
'ping-exit',
'ping-restart',
'ping-timer-rem:',
'ping',
'fast-io',
'remap-usr1',
'persist-remote-ip',
'persist-local-ip',
'tun-mtu',
'tun-mtu-extra',
'link-mtu',
'mtu-disc',
'mtu-test',
'fragment',
'mssfix',
'sndbuf',
'rcvbuf',
'txqueuelen',
'mlock',
'up',
'up-delay',
'down',
'down-pre',
'up-restart',
'disable-occ',
'comp-noadapt',
'auth-retry',
'explicit-exit-notify',
'auth',
'cipher',
'prng',
'keysize',
'engine',
'no-replay',
'mute-replay-warnings',
'replay-window',
'no-iv',
'replay-persist',
'key-method',
'capath',
'tls-cipher',
'tls-timeout',
'reneg-bytes',
'reneg-pkts',
'reneg-sec',
'hand-window',
'tran-window',
'single-session:',
'tls-exit',
'pkcs11-providers',
'pkcs11-protected-authentication',
'pkcs11-private-mode',
'pkcs11-cert-private',
'pkcs11-pin-cache',
'pkcs11-id-management',
'pkcs11-id',
'win-sys',
'ip-win32',
'route-method',
'dhcp-option',
'dhcp-renew',
'dhcp-pre-release',
'dhcp-release',
'tap-sleep',
'pause-exit',
]
