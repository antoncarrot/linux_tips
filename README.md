# Linux tips

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

### CentOS update
```bash
yum check-update
yum update
```

### Docker update container
```bash
docker ps
docker stop <ID>
docker rm <ID>
docker pull <name>
docker run ...
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
