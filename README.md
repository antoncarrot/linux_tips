# Linux tips

### Firefox about:config

```
browser.sessionstore.interval	120000
mousewheel.acceleration.start	1
mousewheel.acceleration.factor	2
```

### Set file and dir chmod

```
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
```

### Set init level 3

```bash
systemctl set-default runlevel3.target
```

### Show net interfaces

```bash
ip link show
```

### Install ifconfig

```bash
apt-get install net-tools
```

### Set interfaces manualy

Edit /etc/network/interfaces

```bash
auto enp0s3
iface enp0s3 inet static
	address 10.0.2.15
	netmask 255.255.255.0
	gateway 10.0.2.2
```

### Allow root login via ssh

Edit /etc/ssh/sshd_config

```bash
PermitRootLogin yes
```

### Run graphical applications without a display

```bash
apt-get install xvfb
Xvfb :99 &
export DISPLAY=:99
```

or

```bash
xvfb-run <cmd>
```

### Monitor wakes up immediately after suspend

Disable monitor auto select input source

### Restart bluetooth and monitors after suspend

Create scripts in /lib/systemd/system-sleep/

```bash
#!/bin/bash

if [ "${1}" == "post" ]; then
sleep 1
/usr/bin/systemctl stop bluetooth.service
sleep 2
/usr/bin/systemctl start bluetooth.service
fi

exit 0
```

```bash
#!/bin/bash

if [ "${1}" == "post" ]; then
export XAUTHORITY="/var/run/lightdm/root/:0"
export DISPLAY=":0"
sleep 1
xset dpms force standby
sleep 2
xset dpms force on
fi

exit 0
```

### GRUB

/etc/default/grub

add to GRUB_CMDLINE_LINUX_DEFAULT=

```
mitigations=off
```

```
sudo update-grub
```

### Mint snapd

```
sudo rm /etc/apt/preferences.d/nosnap.pref
```

### Mint del unused

```
sudo apt-get purge thunderbird warpinator onboard onboard-common gnote pix pix-data drawing hexchat hexchat-common webapp-manager celluloid hypnotix rhythmbox rhythmbox-data
```

### VPNC

```
sudo apt-get install network-manager-vpnc-gnome
```

### DNS for vpn

```
sudo vim /etc/NetworkManager/system-connections/<name>.nmconnection
```

```
dns-search=~.
```

### DNS status

```
resolvectl dns

systemd-resolve --status
```

### Cinnamon unset ctrl alt shift up

```
gsettings set org.cinnamon.desktop.keybindings.wm move-to-workspace-up []
gsettings set org.cinnamon.desktop.keybindings.wm move-to-workspace-down []
```

### ssh port forward

```
ssh -X -L 1433:127.0.0.1:1433 -L 1521:127.0.0.1:1521 <user>@<host> -p <port>
```

### docker ssl error

```
sudo vim /etc/systemd/system/docker.service.d/env.conf
```

```
[Service]
Environment="GODEBUG=x509ignoreCN=0"
```

```
sudo systemctl show --property=Environment docker
```
