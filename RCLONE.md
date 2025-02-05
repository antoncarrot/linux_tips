###

`rclone bisync gdrive: ~/gdrive/ -MvP --compare size,modtime,checksum --conflict-resolve newer --conflict-loser delete --recover`

`~/.config/systemd/user/rclone.service`

`~/.config/systemd/user/rclone.timer`

`~/.config/systemd/user/rclone.path`

```
systemctl --user daemon-reload
systemctl --user enable --now rclone.{timer,path,service}
```

```
systemctl --user status rclone.service rclone.timer rclone.path
journalctl --user -xeu rclone.service rclone.timer rclone.path
```

