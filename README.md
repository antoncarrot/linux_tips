# Linux tips

### 1. Set init level 3

```bash
systemctl set-default runlevel3.target
```

### 2. Show net interfaces

```bash
ip link show
```

### 3. Install ifconfig

```bash
apt-get install net-tools
```

### 4. Set interfaces manualy

Edit /etc/network/interfaces

```bash
auto enp0s3
iface enp0s3 inet static
	address 10.0.2.15
	netmask 255.255.255.0
	gateway 10.0.2.2
```

### 5. Allow root login via ssh

Edit /etc/ssh/sshd_config

```bash
PermitRootLogin yes
```

### 6. Run graphical applications without a display

```bash
apt-get install xvfb
Xvfb :99 &
export DISPLAY=:99
```

or

```bash
xvfb-run <cmd>
```
