building..

### Startup items settings

    BIOS = seaBIOS
    virtIO SCSI
### Initialization settings([archlinux](https://mirrors.ustc.edu.cn/archlinux/images/))

    mkdir workspace && wget https://mirrors.ustc.edu.cn/archlinux/images/v20230301.130409/Arch-Linux-x86_64-basic-20230301.130409.qcow2
    cd workspace/ && mv Arch-Linux-x86_64-basic-20230301.130409.qcow2 archlinux.qcow2
    sudo qm importdisk 100 archlinux.qcow2 SATA250
    sudo qm disk resize 100 scsi0 70G
### BIOS settings

    'e' to edit
    search 'Linux' go to the end, write 'init=/bin/bash'
    ctrl + x
    mount -n -o remount，rw /
    passwd
    reboot
### Configure a static IP address

    pacman -Syy && pacman -S vim
    vim /etc/systemd/network/xx.network
    [Network]
    Address=192.168.20.100/24
    Gateway=192.168.20.2
    DNS=8.8.8.8
    DNS=8.8.4.4
### Sddm login settings

    vim /usr/lib/sddm/sddm.conf.d/default.conf
    # Comma-separated list of users that should not be listed
    HideUsers=sync
    # Maximum user id for displayed users
    MaximumUid=60000
    # Minimum user id for displayed users
    MinimumUid=0
    
    vim /etc/pam.d/sddm
    #auth    required        pam_succeed_if.so user != root quiet_success
    auth    sufficient      pam_succeed_if.so user ingroup nopasswdlogin
### Freerdp install

point to the client

    pacman -S krdc freerdp
point to the server

    yay -S xrdp xorgxrdp-glamor pulseaudio-module-xrdp
    
